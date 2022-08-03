from django.urls import path,include
from . import views 

urlpatterns = [
    path("",views.RegisterPage,name="registerpage"),
    path("register/",views.UserRegister,name="userregister"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("userlogin/",views.UserLogin,name="login"),
    path("uploadpage/",views.UploadPage,name="upload"),
    path("upload/",views.UploadImage,name="imageupload"),
    path("showimage/",views.ImageFetch,name="showimage")
]
 