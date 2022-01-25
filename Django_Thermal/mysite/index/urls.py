from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path('wsq',views.index, name="index"),\
  path('index.html',views.index, name="index"),
  path('live/data/', views.DataTable, name="DataTable"),

]
