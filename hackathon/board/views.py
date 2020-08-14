from django.shortcuts import render

# Create your views here.
def board(request, category) :
    # category : secondhand || room
    print(category)
    items = []
    return render(request, 'board.html', {'category' : category,
                                            'items' : items})