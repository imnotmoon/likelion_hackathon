from django.shortcuts import render
from usedtrading.models import Usedtrading
from bang.models import Bang

# Create your views here.
def board(request, category) :
    # category : secondhand || room
    print(category)
    if category == 'usedtrading':
        items = Usedtrading.objects.all()
    elif category == 'bang':
        items = Bang.objects.all()
    return render(request, 'board.html', {'category' : category,
                                                'items' : items})