from django.shortcuts import render,redirect
from Admin_Panel.views import *
from Admin_Panel.models import *

# Create your views here.

def index1(request):
    msg = ""
    msg1=""
    # Slider = admin_slider.objects.order_by('-id')[:3].all()
    comment = comments.objects.order_by('-id')[:4].all()
    # Slider1 = admin_slider.objects.order_by('-id')[1]
    # Slider2 = admin_slider.objects.order_by('-id')[1]
    food_category1 = food_category.objects.all() 
    food1 = food.objects.order_by('-id')[:10].all()
    obj = tablebook_form()
    if 'save' in request.POST:
        obj = tablebook_form(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Thank You"
            
    obj1 = comments_form()
    if 'send' in request.POST:
        obj1 = comments_form(request.POST,request.FILES)
        if obj1.is_valid():
            obj1.save()
            msg1 = "Thank You For Review"
    return render(request,'index.html', {'food_category':food_category1,'food':food1,'msg':msg,'msg1':msg1,'comment':comment})
# 'slid1':Slider1,'slid2':Slider2,'slider':Slider,

def about1(request):
    return render(request,'about.html')

def menu1(request):
    food_category1 = food_category.objects.all()
    food1 = food.objects.all() 
    return render(request,'menu.html',{'food_category':food_category1,'food':food1})

def book1(request):
    msg = ""
    obj = tablebook_form()
    if 'save' in request.POST:
        obj = tablebook_form(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Thank You"
    return render(request,'book.html',{'msg':msg,'frm':obj})