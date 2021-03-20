from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
# Create your views here.
def Index(request):
    pro1 = Product.objects.all()
    # return HttpResponse("<h1>Hello</h1>")
    return render(request,'index.html',{'pro2' : pro1})
    
