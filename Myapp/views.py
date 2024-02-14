from django.shortcuts import render,redirect
from Myapp.models import Genre,Movie
from Myapp.forms import Genreform,Movieform,Register,Login
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.utils.decorators import method_decorator
def Signin(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request, *args, **kwargs)
        else:
            return redirect("Login")
    return wrapper


class Registerform(View):
    def get(self,request,*args,**kwargs):
        count=User.objects.count()
        print(count)
        if count<2:
            rform=Register()
            return render(request,"regform.html",{"rf":rform}) 
        else:
            messages.error(request,"Sorry the registration is full")
            return redirect("Login")
        
    def post(self,request,*args,**kwargs):
        rform=Register(request.POST)
        if rform.is_valid():
            messages.success(request,"Registration successful")
            User.objects.create_user(**rform.cleaned_data)
        else:
            messages.error(request,"Invalid details ")
        return redirect("Login")


class Loginview(View):
    def get(self,request,*args,**kwargs):
        lform=Login()
        return render(request,"logform.html",{"lf":lform})
    def post(self,request,*args,**kwargs):
        lform=Login(request.POST)
        if lform.is_valid():
            username=lform.cleaned_data.get("username")
            password=lform.cleaned_data.get("password")
            obj=authenticate(username=username,password=password)
            if obj:
                login(request,obj)
                messages.success(request,"You have logged in successfully ")
                return redirect("gtable")
            
            else:
                messages.error(request,"Invalid credentials")
                return redirect("Login")
        else:
            return render(request,"logform.html",{"lf":lform}) 
        
class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Successflly logged out.Please login to continue")
        return redirect("Login")
@method_decorator(Signin,name="dispatch")
class Genreview(View):
    def get(self,request,*args,**kwargs):
        gform=Genreform()
       
        return render(request,"genreform.html",{"gf":gform})
    def post(self,request,*args,**kwargs):
        gform=Genreform(request.POST)
        if gform.is_valid():
            messages.success(request,"Movie details entered successfully ")
            Genre.objects.create(**gform.cleaned_data)
        else:
            messages.error(request,"Invalid details ")
        return redirect("gtable")
@method_decorator(Signin,name="dispatch")        
class Genretable(View):    
    def get(self,request,*args,**kwargs):
        details=Genre.objects.all()
        return render(request,"gtable.html",{"d":details})
    def post(self,request,*args,**kwargs):
        genrename=request.POST.get("hi")
        print(id)
        details=Genre.objects.filter(genrename=genrename)
        return render(request,"gtable.html",{"d":details})
class Genresingleview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        details=Genre.objects.get(id=id)
        return render(request,"gsingle.html",{"d":details})
class Genremoveview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        genredetails=Genre.objects.get(id=id)
        moviedetails=Movie.objects.filter(genre_id=id)
        return render(request,"genremovie.html",{"g":genredetails,"m":moviedetails})

class Genreupdate(View):
    def get(self,request,*args,**kwargs):
         upid=kwargs.get("pk")
         updetails=Genre.objects.get(id=upid)
         gform=Genreform(instance=updetails)
         return render(request,"gedit.html",{"gf":gform})
    def post(self,request,*args,**kwargs):
        upid=kwargs.get("pk")
        updetails=Genre.objects.get(id=upid)
        gform=Genreform(request.POST,instance=updetails)
        if gform.is_valid():
            gform.save()
            messages.success(request,"Updation successful")
        else:
            messages.error(request,"unsuccessful updation")
        return redirect("gtable")

class Genredelete(View):
    def get(self,request,*args,**kwargs):
        delid=kwargs.get("pk")
        Genre.objects.get(id=delid).delete()
        return redirect("gtable")
@method_decorator(Signin,name="dispatch")
class Movieview(View):
    def get(self,request,*args,**kwargs):
        mform=Movieform()
        return render(request,"mform.html",{"mf":mform})
    def post(self,request,*args,**kwargs):
        mform=Movieform(request.POST,files=request.FILES)
        if mform.is_valid():
            messages.success(request,"Movie details entered successfully ")
            mform.save()
        else:
            messages.error(request,"Invalid details ")
        return redirect("mtable")
@method_decorator(Signin,name="dispatch")   
class Movietable(View):
    def get(self,request,*args,**kwargs):
        mtable=Movie.objects.all()
        

        return render(request,"mtable.html",{"mt":mtable})
    def post(self,request,*args,**kwargs):
        genrename=request.POST.get("hi")
        print(id)
        details=Genre.objects.filter(genrename=genrename)
        return render(request,"gtable.html",{"d":details})   
class Moviesingle(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get("pk")
        
        sdetails=Movie.objects.get(id=sid)
        return render(request,"msingle.html",{"s":sdetails})
class Movieedit(View):
    def get(self,request,*args,**kwargs):
        editid=kwargs.get("pk")
        editdetails=Movie.objects.get(id=editid)
        mform=Movieform(instance=editdetails)
        return render(request,"medit.html",{"mf":mform})
    def post(self,request,*args,**kwargs):
        editid=kwargs.get("pk")
        editdetails=Movie.objects.get(id=editid)
        mform=Movieform(request.POST,files=request.FILES,instance=editdetails)
        if mform.is_valid():
            mform.save()
            messages.success(request,"Movie details edited successfuly")
        else:
            messages.error(request,"unsuccessful updation")
        return redirect("mtable")
    
class Movidelete(View):
    def get(self,request,*args,**kwargs):
        delid=kwargs.get("pk")
        Movie.objects.get(id=delid).delete()
        return redirect("gtable")