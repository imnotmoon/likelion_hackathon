from django.shortcuts import render
from usedtrading.models import Usedtrading

# Create your views here.
def board(request, category) :
    # category : secondhand || room
    print(category)
    items = Usedtrading.objects.all()
    return render(request, 'board.html', {'category' : category,
                                            'items' : items})