"""
URL configuration for Assignment_Movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Myapp.views import Genreview,Movieedit,Genresingleview,Movidelete,Moviesingle,Genremoveview,Registerform,Loginview,Logout,Genretable,Genreupdate,Movietable,Movieview,Genredelete
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("Register/",Registerform.as_view(),name="register"),
    path("",Loginview.as_view(),name="Login"),

    path("Welcome/",Loginview.as_view(),name="Welcome"),
    path("genre/",Genreview.as_view(),name="genre"),
    path("gtable/",Genretable.as_view(),name="gtable"),
    path("gtable/<int:pk>/edit",Genreupdate.as_view(),name="gedit"),
    path("gtable/<int:pk>/Single",Genresingleview.as_view(),name="single"),
    path("gtable/<int:pk>/genremovie",Genremoveview.as_view(),name="genremovie"),

     path("gtable/<int:pk>/delete/",Genredelete.as_view(),name="delete"),
     path("mform/",Movieview.as_view(),name="mform"),
     path("mtable/",Movietable.as_view(),name="mtable"),
     path("msingle/<int:pk>",Moviesingle.as_view(),name="msingle"),
     path("mtable/<int:pk>/edit",Movieedit.as_view(),name="medit"),
     path("mtable/<int:pk>/delete",Movidelete.as_view(),name="delete"),
     path("logout/",Logout.as_view(),name="Logout"),
      
     

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
