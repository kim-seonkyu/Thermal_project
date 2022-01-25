from django.shortcuts import render
from .models import TempData
from django.http.response import JsonResponse

# Create your views here.

def tables(request):
  return render(
    request, "tables/tables.html")
    
def DataTable(request):
    queryset = TempData.objects.all()
    return JsonResponse({"users": list(queryset.values())})
