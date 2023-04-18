from turtle import home
from django.urls import path 
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages #import messages

from . import views 

urlpatterns=[
    path('sidebar',views.sidebar,name='sidebar'),
    path('dashboard',views.dashboard,name='dashboard'),
   
    path('doctor_index',views.doctor_index,name='doctor_index'),
    path('doctor_event',views.doctor_event,name='doctor_event'),
    path('doctor_event_booking',views.doctor_event_booking,name='doctor_event_bookingentries'),
    
    path('doctor_content',views.doctor_content,name='doctor_content'),
    path('doctor_contenttype',views. doctor_contenttype,name='contenttype'),
    
    path('doctor_feedback',views.doctor_feedback,name='doctor_feedback'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('forgotpasswordprocess',views.forgotpasswordprocess,name='forgotpassword'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('changepasswordprocess',views.changepasswordprocess,name='changepassword'),
  
    
    path('doctor_index1',views.doctor_index1,name='doctor_index1'),
    path('doctor_login',views.doctor_login,name='doctor_login'),
    path('doctor_profile',views.doctor_profile,name='doctor_profile'),
    path('register', views.register, name="register"),
    path('register/inserted', views.registeraddprocess, name="registeraddprocess"),
   
    path('doctor_booking',views.doctor_booking,name='doctor_booking'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('profile',views.profile,name='profile'),
    
    

    
]