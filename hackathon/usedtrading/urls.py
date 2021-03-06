from django.urls import path
from . import views

urlpatterns = [
    path('usedhome/',views.usedhome, name ='usedhome'),
    path('create/',views.create, name = 'create'),
    path('usednew/',views.usednew, name = 'usednew'),
    path('<int:usedtrading_id>/',views.useddetail,name ='useddetail'),
    path('<int:usedtrading_id>/useddelete/',views.useddelete, name= 'useddelete'),
    path('<int:usedtrading_id>/usedupdate/',views.usedupdate, name= 'usedupdate'),
]