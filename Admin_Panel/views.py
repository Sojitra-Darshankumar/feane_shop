from django.shortcuts import render,redirect
from django.http import HttpResponse
from Admin_Panel.models import *
import random
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


def admin_index(request):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request,'admin-index.html',{'info':info})

def admin_login(request):
    msg = ""
    if 'login' in request.POST:
       
        Email = request.POST['email']
        Password = request.POST['password']
        rows = admin_registration.objects.filter(email=Email,password=Password)
       
        print(rows.count())
        if rows.count() == 0:
            msg = "Invalid E-Mail Or Password"
        else:
            user = rows.first()
            request.session['adminid'] = user.id
            print(user)
            msg = "Success"
            return redirect("/index/")
    return render(request,'admin-login.html',{'msg':msg})

def logout(request):
    del request.session['adminid']
    return redirect('/admin-login/')

# ------------------------------------------------------------------------- Admin -------------------------


def admin_registration1(request):
    msg = ""
    obj = admin_registration_form()
    if 'save' in request.POST:
        obj = admin_registration_form(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Successfull"
            return redirect('/admin-login/')
    return render(request,'admin-register.html',{'msg':msg,'frm':obj})

def admin_view(request):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    admin = admin_registration.objects.filter().all()
    print(admin)
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request, 'admin-view.html' , {'admin_detail' : admin , 'info':info}) 

def add_admin(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    obj = admin_registration_form()
    if 'save' in request.POST:
        obj = admin_registration_form(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/admin-view/')
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request,'admin-add.html',{'msg':msg ,'info':obj , 'info':info})


def admin_edit(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    info=admin_registration.objects.filter(id=edit_id).get()
    obj=admin_registration_form(instance=info)
    msg=""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    else:
        if 'save' in request.POST:
            obj=admin_registration_form(request.POST,request.FILES,instance=info)
            if obj.is_valid():
                obj.save()
                msg="data update"
                return redirect("/admin-view/")
            print(info)         
    adminid = request.session['adminid']
    info1 = admin_registration.objects.filter(id=adminid).get()
    return render(request,'admin-add.html',{'admin_edit':info,'msg':msg,'info':info1})

def delete_view_admin(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    admin_registration.objects.get(id=del_id).delete()
    return redirect('/admin-view/')

# ------------------------------------------------------------------------- Slider -------------------------

# def add_slider(request):
#     msg = ""
#     if 'adminid' not in request.session:
#         return redirect('/admin-login/')
#     obj = admin_slider_form()
#     if 'save' in request.POST:
#         obj = admin_slider_form(request.POST,request.FILES)
#         obj.save()
#         msg = "Successfull" 
#         return redirect('/slider-view/')
#     adminid = request.session['adminid']
#     info = admin_registration.objects.filter(id=adminid).get()
#     return render(request,'slider-add.html',{'msg':msg , 'info':info})


# def slider_edit(request,edit_id):
#     if 'adminid' not in request.session:
#         return redirect('/admin-login/')
#     info=admin_slider.objects.filter(id=edit_id).get()
#     obj=admin_slider_form(instance=info)
#     msg=""
#     if 'save' in request.POST:
#         obj=admin_slider_form(request.POST,request.FILES,instance=info)
#         if obj.is_valid():
#             obj.save()
#             msg="data update"
#             return redirect("/slider-view/")
#         print(info)
        
#     adminid = request.session['adminid']
#     info1 = admin_registration.objects.filter(id=adminid).get()
#     return render(request,'slider-add.html',{'slider_edit':info,'msg':msg,'info':info1})

# def delete_view_slider(request,del_id):
#     if 'adminid' not in request.session:
#         return redirect('/admin-login/')
#     admin_slider.objects.get(id=del_id).delete()
#     return redirect('/slider-view/')

# def slider_view(request):
#     if 'adminid' not in request.session:
#         return redirect('/admin-login/')
#     slider = admin_slider.objects.filter().all()
#     print(slider)
#     adminid = request.session['adminid']
#     info = admin_registration.objects.filter(id=adminid).get()
#     return render(request, 'slider-view.html' , {'slider_detail' : slider , 'info':info}) 


# ------------------------------------------------------------------------- Food Category -------------------------

def add_food_category(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    obj = food_category_form()
    if 'save' in request.POST:
        obj = food_category_form(request.POST,request.FILES)
        obj.save()
        msg = "Successfull" 
        return redirect('/food_category_view/')
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request,'food-category-add.html',{'msg':msg , 'info':info})


def food_category_edit(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    info=food_category.objects.filter(id=edit_id).get()
    obj=food_category_form(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=food_category_form(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/food_category_view/")
        print(info)
    adminid = request.session['adminid']
    info1 = admin_registration.objects.filter(id=adminid).get()
    return render(request,'food-category-add.html',{'food_category_edit':info,'msg':msg,'info':info1})

def delete_view_food_category(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    food_category.objects.get(id=del_id).delete()
    return redirect('/food_category_view/')

def food_category_view(request):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    food_category1 = food_category.objects.filter().all()
    print(food_category1)
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request, 'food-category-view.html' , {'food_category_detail' : food_category1 , 'info':info}) 

# ------------------------------------------------------------------------------------------------------------------ Food ------------------

def add_food(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    all_cat = food_category.objects.all()
    obj = food_form()
    if 'save' in request.POST:
        obj = food_form(request.POST,request.FILES)
        obj.save()
        msg = "Successfull" 
        return redirect('/food_view/')
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request,'food-add.html',{'msg':msg , 'info':info , 'all_cats':all_cat,'frm':obj})


def food_edit(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    all_cat = food_category.objects.all()
    info=food.objects.filter(id=edit_id).get()
    obj=food_form(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=food_form(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/food_view/")
        print(info)
    adminid = request.session['adminid']
    info1 = admin_registration.objects.filter(id=adminid).get()
    return render(request,'food-add.html',{'food_edit':info,'msg':msg, 'all_cats':all_cat,'info':info1})

def delete_view_food(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    food.objects.get(id=del_id).delete()
    return redirect('/food_view/')

def food_view(request):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    food1 = food.objects.filter().all()
    food_category1 = food_category.objects.filter().all()
    print(food1)
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request, 'food-view.html' , {'food_detail' : food1 , 'info':info ,'food_category':food_category1})

# ------------------------------------------------------------------------------ Table Book ----------------------

def table_book_view(request):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    table_book = tablebook.objects.filter().all()
    print(table_book)
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request, 'book-table.html' , {'table_detail' : table_book , 'info':info})

# ------------------------------------------------------------------------------ Comments ----------------------

def comment_view(request):
    if 'adminid' not in request.session:
        return redirect('/admin-login/')
    comment = comments.objects.filter().all()
    print(comment)
    adminid = request.session['adminid']
    info = admin_registration.objects.filter(id=adminid).get()
    return render(request, 'comment-view.html' , {'comment_detail' : comment , 'info':info})

def ajax_search_admin(request):
    searchkeyword = request.GET['search_admin']
    searchby = request.GET['search_by']
    if searchby=="name":
        data = admin_registration.objects.filter(username__contains=searchkeyword).all()
    elif searchby=="email":
        data = admin_registration.objects.filter(email__contains=searchkeyword).all()
    elif searchby=="id":
        data = admin_registration.objects.filter(id=searchkeyword).all()
    elif searchby=="contact":
        data = admin_registration.objects.filter(contact__contains=searchkeyword).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr style="text-align: center;"><td>'+str(row.id)+'</td><td><img src="'+row.Photo.url+'" alt="" width="30px" height="30px" style="object-fit: cover; border-radius:100%;"></td><<td>'+row.username+'</td><td>'+row.email+'</td><td>'+str(row.contact)+'</td><td>'+str(row.password)+'</td><td><div class="input3"><div class="ic"><a href="/admin_edit/'+str(row.id)+'" style="text-decoration: none;"><button type="button" class="btn btn-primary">EDIT<i class="mdi mdi-eyedropper-variant"></i></button></a></div><div class="name"><a href="/delete_view_admin/'+str(row.id)+'" style="text-decoration: none;"><button type="button" class="btn btn-danger">DELETE<i class="mdi mdi-delete-sweep"></i></button></a></div></div></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_slider(request):
    searchkeyword = request.GET['search_slider']
    searchby = request.GET['search_by']
    if searchby=="off":
        data = admin_slider.objects.filter(off=searchkeyword).all()
    elif searchby=="title":
        data = admin_slider.objects.filter(title__contains=searchkeyword).all()
    elif searchby=="id":
        data = admin_slider.objects.filter(id=searchkeyword).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr style="text-align: center;"><td>'+str(row.id)+'</td><td>'+row.title+'</td><td>'+str(row.off)+'</td><td><textarea cols="50" rows="5" style="background-color: #191c24; color: #6c7293; border: none; text-align: center; ">'+row.description+'</textarea></td><td><div class="input3"><div class="ic"><a href="/slider_edit/'+str(row.id)+'" style="text-decoration: none;"><button type="button" class="btn btn-primary">EDIT<i class="mdi mdi-eyedropper-variant"></i></button></a></div><div class="name"><a href="/delete_view_slider/'+str(row.id)+'" style="text-decoration: none;"><button type="button" class="btn btn-danger">DELETE<i class="mdi mdi-delete-sweep"></i></button></a></div></div></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_food_category(request):
    searchkeyword = request.GET['search_food_category']
    searchby = request.GET['search_by']
    if searchby=="title":
        data = food_category.objects.filter(title__contains=searchkeyword).all()
    elif searchby=="id":
        data = food_category.objects.filter(id=searchkeyword).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr style="text-align: center;"><td>'+str(row.id)+'</td><td>'+row.title+'</td><td><div class="input3"><div class="ic"><a href="/food_category_edit/'+str(row.id)+'" style="text-decoration: none;"><button type="button" class="btn btn-primary">EDIT<i class="mdi mdi-eyedropper-variant"></i></button></a></div><div class="name"><a href="/delete_view_food_category/'+str(row.id)+'" style="text-decoration: none;"><button type="button" class="btn btn-danger">DELETE<i class="mdi mdi-delete-sweep"></i></button></a></div></div></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_food(request):
    searchkeyword = request.GET['search_food']
    searchby = request.GET['search_by']
    serchbycategory = request.GET["serch_by_food_category"]
    if searchby=="title":
        if serchbycategory!="":
            data = food.objects.filter(title__contains=searchkeyword,food_category=serchbycategory).all()
        else:
            data = food.objects.filter(title__contains=searchkeyword).all()
    elif searchby=="id":
        data = food.objects.filter(id=searchkeyword).all()
    elif searchby=="food_category":
        data = food.objects.filter(food_category=searchkeyword).all()
    elif searchby=="price":
        data = food.objects.filter(price=searchkeyword).all()
    elif searchby=="admin_id":
        data = food.objects.filter(admin_id=searchkeyword).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr style="text-align: center;"><td>'+str(row.id)+'</td><td>'+row.title+'</td><td><textarea cols="50" rows="5" style="background-color: #191c24; color: #6c7293; border: none; text-align: center; ">'+row.description+'</textarea></td><td>'+str(row.price)+'</td><td>'+str(row.food_category)+'</td><td>'+str(row.admin_id)+'</td><td><img src="'+row.photo.url+'" alt="" width="30px" height="30px" style="object-fit: cover; border-radius:100%;"></td><td><div class="input3"><div class="ic"><a href="/food_edit/'+str(row.id)+'" style="text-decoration: none;"><button type="button" class="btn btn-primary">EDIT<i class="mdi mdi-eyedropper-variant"></i></button></a></div><div class="name"><a href="/delete_view_food/'+str(row.id)+'" style="text-decoration: none;"><button type="button" class="btn btn-danger">DELETE<i class="mdi mdi-delete-sweep"></i></button></a></div></div></td></tr>'
    return HttpResponse(htmlData)

    # --------------------------------------------------- Forgot Password By Email ------------

def forgot_password_email(request):
    msg = ""
    if 'forgot' in request.POST:
        email = request.POST['email']
        rows = admin_registration.objects.filter(email=email)
        print(rows.count())
        if rows.count() == 0:
            msg = "Invalid E-Mail"
        else:
            user = rows.first()
            # request.session[''] = user.id
            otp = random.randint(000000,999999)
            request.session['otp'] = otp
            send_mail(
                    subject="FEANE - Request For OTP",
                    message="Hello Dear User You Can Send The Request For Reset Your Password <br>,Your OTP Is : "+str(otp),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )
            request.session['forgotid'] = user.id
            print(user)
            return redirect("/verify_otp/")
    return render(request,'forgot-password.html',{'msg':msg})

# ------------------------------------------------------------------------ Verify OTP ------------

def verify_otp(request):  
    msg=""
    if 'verify' in request.POST:
        user_otp = request.POST['user_otp']
        otp_session = str(request.session['otp'])
        if user_otp == otp_session:
            return redirect('/recover_password/')
        else:
            msg = "invelid OTP"
    return render(request,'otp-verify.html',{'msg':msg})

# ------------------------------------------------------------------- Recover Password ------------

def recover_password(request):
    msg=""
    if 'save' in request.POST:
        password1 = request.POST['Password']
        password2 = request.POST['Retype_Password']
        user_id = request.session['forgotid']
        if password1 == password2:  
            info=admin_registration.objects.filter(id = user_id).get()
            info.password = password1
            info.save()
            msg="data update"
            return redirect("/admin-login/")
        else:
            msg="Both Password Is Not Match"
    return render(request,'recover-password.html',{'msg':msg})