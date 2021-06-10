from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect



# Create your views here.
def register(request):
    if request.method =='POST':
        uname=request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword= request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exist")
                return redirect('register')

            elif User.objects.filter(first_name=fname).exists():
                messages.info(request,"firstname already exist")
               # return redirect('register')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                #return redirect('register')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=uname, password=password, first_name=fname, last_name=lname,
                                            email=email)
                user.save();
                return redirect('login')



                print("user created")
        else:
            messages.info(request,"password not matching")
        return render(request,'register.html')
    return render(request,"register.html")
def login(request):
    if request.method =='POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')