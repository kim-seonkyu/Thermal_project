from django.shortcuts import render

# Create your views here.

def imgs(request):
  return render(
    request, "imgs/imgs.html")

