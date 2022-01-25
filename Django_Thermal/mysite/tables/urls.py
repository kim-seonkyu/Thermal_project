from django.urls import path

from . import views

urlpatterns = [
    path('',views.tables, name="tables"),\
    path('tables.html/', views.tables, name="tables"),
]