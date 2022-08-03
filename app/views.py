from email import message
from email.errors import MessageError
from email.mime import image
from django.forms import EmailField
from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def RegisterPage(request):
    return render(request,"app/register.html")


#view for user reg
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        images = request.FILES['images']

 

        #check user already exist or not
        user = User.objects.filter(Email=email)

        if user:
            message = "user already exist!!"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser= User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password,Images=images)
                message = "User Successfully registered!"
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "please input same password"
                return render(request,"app/register.html",{'msg':message})
 
 #log in page view

def LoginPage(request):
    return render(request,"app/login.html")

#view for sign in with validation
def UserLogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        #check user already exist or not
                
        if User.objects.filter(Email=email): 
            user = User.objects.get(Email=email) 
            if user:
                 if user.Password == password:
                    request.session['Firstname']=user.Firstname
                    request.session['Lastname']=user.Lastname
                    request.session['Email']=user.Email
                    all_img = User.objects.get(Images=image)
                    return render(request,"app/home.html",{'key1':all_img})
                 else:
                    message = "password doesn't match"
                    return render(request,"app/login.html",{'msg':message})
        else:
            message = "user doesn't exist!"
            return render(request,"app/register.html",{'msg':message})

 # view upload page
def UploadPage(request):
    return render(request,"app/upload.html")

#upload image view
def UploadImage(request):
    if request.method=='POST':
        imagename = request.POST['imgname']
        pics = request.FILES['images']

        newimg = Image.objects.create(Imagename=imagename,Image=pics)
        return redirect('showimage')

# image fetching
def ImageFetch(request):
    all_img = Image.objects.all()
    return render(request,"app/showImage.html",{'key1':all_img})