from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '유저이름이나 비밀번호가 잘못 되었습니다.'})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["passwordconfig"]:
            user = User.objects.create_user(username=request.POST["username"],password=request.POST["password"])
            fullname = request.POST["fullname"]
            ssd = request.POST['ssd']
            profile = Profile(user=user, fullname=fullname,ssd=ssd)
            profile.save()
            auth.login(request,user)
            return redirect('/')
    return render(request, 'signup.html')