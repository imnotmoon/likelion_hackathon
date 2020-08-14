from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Usedtrading
# Create your views here.
def usedhome(request):

    return render(request,'usedhome.html')

def usednew(request):
    return render(request, 'usednew.html')

def create(request):
    usedtrading = Usedtrading()
    usedtrading.title = request.POST['title']
    usedtrading.body = request.POST['body']
    usedtrading.cost = request.POST['cost']
    #image
    usedtrading.images  = request.FILES.get('images',None)
    usedtrading.image2  = request.FILES.get('image2',None)
    usedtrading.image3  = request.FILES.get('image3',None)
    usedtrading.writer = request.POST['writer']
    if usedtrading.images is None:
        return render(request, 'new.html',{'error': 'please input images'})
    else:

        usedtrading.pub_date = timezone.datetime.now()
    
        usedtrading.save()
        #알림메세지 추가
        messages.success(request, 'Success to Upload')
        return redirect('/usedtrading/usedhome')