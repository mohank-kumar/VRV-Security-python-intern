from django.shortcuts import redirect, render
from . models import *
from django.contrib import messages

def home(request):
    return render(request,'shop/index.html')

def register(request):
    return render(request,'shop/register.html')

def collections(request):
    category = catagory.objects.filter(state=0)
    return render(request,'shop/collections.html',{"catagory":category})

def collectionsViews(request,name):
    if(catagory.objects.filter(name=name,state=0)):
          Products=product.objects.filter(catagory__name=name)
          return render(request,'shop/Products/index.html   ',{"Products":Products})
    else:
        messages.warning(request,'No Such Category Found')
        return redirect('collections')
        

