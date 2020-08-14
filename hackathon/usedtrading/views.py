from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Usedtrading
from .forms import UsedtradingUpdate
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def usedhome(request):
    usedtrading = Usedtrading.objects
    
    #Blog를 쿼리셋으로 가져온다.
    blogs_list = Usedtrading.objects.all()
    
    #가져온 걸 1개씩 잘라 페이지를 만든다.
    paginator = Paginator(blogs_list,5)

    #실제로 페이지에 들어갈 내용을 GET.get으로 가져옴
    page = request.GET.get('page')

    #그걸 이제 get_page로써 페이지를 뿌릴 것임.
    articles = paginator.get_page(page)

    return render(request,'usedhome.html',{'usedtrading': usedtrading, 'articles':articles})


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
        return redirect('/usedtrading/usedhome/')

def useddelete(request,usedtrading_id):
    Usedtrading.objects.get(id=usedtrading_id).delete()
    return redirect('/')

def useddetail(request, usedtrading_id):
    usedtrading_detail = get_object_or_404(Usedtrading, pk = usedtrading_id)
    return render(request, 'useddetail.html',{'usedtrading' : usedtrading_detail})


def usedupdate(request, usedtrading_id):
    usedtrading = Usedtrading.objects.get(id = usedtrading_id)
    if request.method =='POST':
        form = UsedtradingUpdate(request.POST)
            
        if form.is_valid():
            usedtrading.title = form.cleaned_data['title']
            usedtrading.body= form.cleaned_data['body']
            usedtrading.cost= form.cleaned_data['cost']
            usedtrading.images = form.cleaned_data['images']
            usedtrading.image2 = form.cleaned_data['image2']
            usedtrading.image3 = form.cleaned_data['image3']
            usedtrading.images = request.FILES['images']
            
            usedtrading.pub_date = timezone.datetime.now()
            usedtrading.save()#DB에 반영하기
            return redirect('/usedtrading/usedhome/')
    else:
        form = UsedtradingUpdate(instance = usedtrading)
        return render(request,'usedupdate.html',{'form':form})