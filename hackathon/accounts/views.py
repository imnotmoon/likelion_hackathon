from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
    if request.method =='POST':
        if request.POST['passwordconfig'] == request.POST['password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'유저이름이 존재합니다'})
            except:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'signup.html',{'error':'비밀번호가 다릅니다.'})
    else:
        return render(request,'signup.html')