"""
URL configuration for feane_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from feane.views import *
from Admin_Panel.views import *

urlpatterns = [
    
    path('', index1),
    path('about/', about1),
    path('book/', book1),
    path('menu/', menu1),

#------------------------------------------------------------------- Admin Panel-------------------

    path('index/',admin_index),
    path('admin-login/',admin_login),
    path('logout/',logout),
    path('admin-registration/',admin_registration1),
    path('admin-view/',admin_view),
    path('add_admin/', add_admin),
    path('admin_edit/<int:edit_id>', admin_edit),
    path('delete_view_admin/<int:del_id>', delete_view_admin),
    # path('add_slider/', add_slider),
    # path('slider_edit/<int:edit_id>', slider_edit),
    # path('delete_view_slider/<int:del_id>', delete_view_slider),
    # path('slider-view/',slider_view),
    path('add_food_category/', add_food_category),
    path('food_category_edit/<int:edit_id>', food_category_edit),
    path('delete_view_food_category/<int:del_id>', delete_view_food_category),
    path('food_category_view/',food_category_view),
    path('add_food/', add_food),
    path('food_edit/<int:edit_id>', food_edit),
    path('delete_view_food/<int:del_id>', delete_view_food),
    path('food_view/',food_view),
    path('table_book_view/',table_book_view),
    path('comment_view/',comment_view),
    path('ajax_search_admin/',ajax_search_admin),
    path('ajax_search_slider/',ajax_search_slider),
    path('ajax_search_food_category/',ajax_search_food_category),
    path('ajax_search_food/',ajax_search_food),
    path('verify_otp/',verify_otp),
    path('recover_password/',recover_password),
    path('forgot_password_email/',forgot_password_email),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
