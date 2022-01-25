from django.shortcuts import render
from django.http.response import JsonResponse
from .models import TempData
# Create your views here.

def index(request):
  return render(
    request,"index/index.html",)

    
def DataTable(request):
    queryset = TempData.objects.all()
    return JsonResponse({"users": list(queryset.values())})
