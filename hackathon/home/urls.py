from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views
from usedtrading import views
urlpatterns= [
    path('usedhome/',include('usedtrading.urls')),
]