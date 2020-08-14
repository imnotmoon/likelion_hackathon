from django.urls import path
from . import views

urlpatterns = [
    path('usedhome/',views.usedhome, name ='usedhome'),
    path('create/',views.create, name = 'create'),
    path('usednew/',views.usednew, name = 'usednew'),
]