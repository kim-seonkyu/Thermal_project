from django.urls import path
from . import views
from . import live_graph

urlpatterns = [
    path('',views.charts, name="charts"),\
    path('charts.html/', views.charts, name="charts"),
    
]