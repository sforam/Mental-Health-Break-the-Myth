from turtle import home
from django.urls import path 
from . import views 

urlpatterns=[
    path('expert_index',views.expert_index,name='expert_index'),
    path('sidebar',views.sidebar,name='sidebar'),
    path('profile',views.profile,name='profile'),
    path('book/', views.booklisting, name="booklisting"),
    path('book/book_delete/<int:id>', views.bookdelete, name="bookdelete"),
    path('book/book_edit/<int:id>', views.bookedit, name="bookedit"),
    path('book/update', views.bookupdate, name="bookupdate"),

    path('register', views.register, name="register"),
    path('register/inserted', views.registeraddprocess, name="registeraddprocess"),
    path('dashboard',views.dashboard,name='dashboard'),
  

    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('forgotpasswordprocess',views.forgotpasswordprocess,name='forgotpassword'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('changepasswordprocess',views.changepasswordprocess,name='changepassword'),
   


    path('com_answer/',views.com_answerlisting,name="com_answerlisting"),
    path('com_answer/create/', views.com_answercreate, name="com_answercreate"),
    path('com_answer/inserted/', views.com_answeraddprocess, name="com_answeraddprocess"),
    path('com_answer/com_answer_delete/<int:id>', views.com_answerdelete, name="com_answerdelete"),
    
    path('com_ques/',views.com_queslisting,name="com_queslisting"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('expert_index1',views.expert_index1,name='expert_index1'),
    path('expert_login',views.expert_login,name='expert_login'),
    path('feedback/',views.feedbacklisting,name='feedbacklisting'),
    path('logout',views.logout,name='logout'),
    
]
    