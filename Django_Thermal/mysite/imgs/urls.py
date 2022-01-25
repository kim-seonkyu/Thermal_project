from django.urls import path

from . import views

urlpatterns = [
    path('',views.imgs, name="imgs"),\
    path('imgs.html/', views.imgs, name="imgs"),
    
]