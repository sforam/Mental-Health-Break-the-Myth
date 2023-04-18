from turtle import home
from django.urls import path 
from . import views 
urlpatterns=[
    path('',views.index3,name='index3'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('changepasswordprocess',views.changepasswordprocess,name='changepassword'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('forgotpasswordprocess',views.forgotpasswordprocess,name='forgotpassword'),
    
    
    path('sidebaruserpanel',views.sidebaruserpanel,name='sidebaruserpanel'),
    path('change_password',views.change_password,name='change_password'),
    
    path('expert1',views.expert1,name='expert1'),
    path('expertdetails/<int:id>',views.expertdetails,name='expert1'),

    path('book_expert/<int:id>',views.book_expert,name='book_expert'),
    path('book_expertprocess',views.book_expert_bhoomikaaddprocess,name='book_expert_bhoomikaaddprocess'),
    path('book_doctor/<int:id>',views.book_doctor,name='book_doctor'),
    path('doctordetails/<int:id>',views.doctordetails,name='doctor1'),

    path('doctor1',views.doctor1,name='doctor1'),
    path('event',views.event,name='event'),
    path('connect',views.connect,name='connect'),
    path('connect/inserted', views.connectaddprocess, name="connectaddprocess"),
   


    path('eventdetails/<int:id>',views.eventdetails,name='eventdetails'),
    path('selfassessment1_test',views.selfassessment1_test,name='selfassessment1_test'),
    path('selfassessment1_test/inserted', views.selfassessment1_testaddprocess, name="selfassessment1_testaddprocess"),
    path('result',views.result,name='result'),
   



    path('event4',views.event4,name='event4'),
    path('whatismentalhealth',views.whatismentalhealth,name='whatismentalhealth'),
    path('event3',views.event3,name='event3'),
    path('event2',views.event2,name='event2'),
    path('videos',views.videos,name='videos'),
    path('resources',views.resources,name='resources'),
  
    path('Grief',views.Grief,name='Grief'),
    path('Addiction',views.Addiction,name='Addiction'),
    path('Anxiety',views.Anxiety,name='Anxiety'),
    path('Depression',views.Depression,name='Depression'),
    path('MoodDisorder',views.MoodDisorder,name='MoodDisorder'),
    path('EatingDisorder',views.EatingDisorder,name='EatingDisorder'),
    path('Stress',views.Stress,name='Stress'),
    path('SleepDisturbances',views.SleepDisturbances,name='SleepDisturbances'),
    path('cdp',views.cdp,name='cdp'),
    path('cdp/inserted', views.cdpaddprocess, name="cdpaddprocess"),
    
    path('feedback',views.feedback,name='feedback'),
    path('feedback/inserted', views.feedbackaddprocess, name="feedbackaddprocess"),
    path('viewfeedback',views.viewfeedback,name='viewfeedback'),
   

    path('doctor',views.doctor,name='doctor'),
    path('nitish',views.nitish,name='nitish'),
    path('book',views.book,name='book'),
    path('register1', views.register1, name="register1"),
    path('register1/inserted', views.registeraddprocess, name="registeraddprocess"),
   


    path('login1',views.login1,name='login1'),
    path('book2',views.book2,name='book2'),
    path('doctor1',views.doctor1,name='doctor1'),
    path('soumya',views.soumya,name='soumya'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('book_doctor_nitish',views.book_doctor_nitish,name='book_doctor_nitish'),
    path('paymentpage',views.paymentpage1,name='paymentpage'),
    path('paymentpage2',views.paymentpage2,name='paymentpage2'),
]  