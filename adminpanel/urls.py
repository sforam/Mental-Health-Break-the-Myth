from turtle import home
from django.urls import path 
from . import views 

urlpatterns=[
    path('sidebar',views.sidebar,name='sidebar'),
    path('admin_index',views.admin_index,name='admin_index'),
    path('user',views.user,name='user'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    
    path('admin_event/', views.eventlisting, name="eventlisting"),
    path('admin_event/create', views.eventcreate, name="eventcreate"),
    path('admin_event/inserted', views.eventaddprocess, name="eventaddprocess"),
    path('admin_event/event_delete/<int:id>', views.eventdelete, name="eventdelete"),
    path('admin_event/event_edit/<int:id>', views.eventedit, name="eventedit"),
    path('admin_event/update', views.eventupdate, name="eventupdate"),

    path('admincommques/', views.cdplisting, name="cdplisting"),
    path('admincommques/cdp_delete/<int:id>', views.cdpdelete, name="cdpdelete"),
    
    path('admincommans/', views.cdpalisting, name="cdpalisting"), 
    path('admincommans/cdpa_delete/<int:id>', views.cdpadelete, name="cdpadelete"),
    
      


    path('admin_eventbook/', views.eventbooklisting, name="eventbooklisting"),
    path('admin_eventbook/create', views.eventbookcreate, name="eventbookcreate"),
    path('admin_eventbook/inserted', views.eventbookaddprocess, name="eventbookaddprocess"),
    path('admin_eventbook/eventbook_delete/<int:id>', views.eventbookdelete, name="eventbookdelete"),
    path('admin_eventbook/eventbook_edit/<int:id>', views.eventbookedit, name="eventbookedit"),
    path('admin_eventbook/update', views.eventbookupdate, name="eventbookupdate"),


    path('adminprofessional/', views.professionallisting, name="professionallisting"),
    path('adminprofessional/create/', views.professionalcreate, name="professionalcreate"),
    path('adminprofessional/inserted/', views.professionaladdprocess, name="professionaladdprocess"),
    path('adminprofessional/professional_delete/<int:id>', views.professionaldelete, name="professionaldelete"),
    path('adminprofessional/professional_edit/<int:id>', views.professionaledit, name="professionaledit"),
    path('adminprofessional/update', views.professionalupdate, name="professionalupdate"),


    path('admin_testque/', views.testlisting, name="testlisting"),
    path('admin_testque/create', views.testcreate, name="testcreate"),
    path('admin_testque/inserted', views.testaddprocess, name="testaddprocess"),
    path('admin_testque/test_delete/<int:id>', views.testdelete, name="testdelete"),
    path('admin_testque/test_edit/<int:id>', views.testedit, name="testedit"),
    path('admin_testque/update', views.testupdate, name="testupdate"),

    path('admin_testanswer/', views.testanswerlisting, name="testanswerlisting"),
   
    path('admin_contenttype/', views.contenttypelisting, name="contenttypelisting"),
    path('admin_contenttype/create', views.contenttypecreate, name="contenttypecreate"),
    path('admin_contenttype/inserted', views.contenttypeaddprocess, name="contenttypeaddprocess"),
    path('admin_contenttype/contenttype_delete/<int:id>', views.contenttypedelete, name="contenttypedelete"),
    path('admin_contenttype/contenttype_edit/<int:id>', views.contenttypeedit, name="contenttypeedit"),
    path('admin_contenttype/update', views.contenttypeupdate, name="contenttypeupdate"),

    path('admin_content/', views.contentlisting, name="contentlisting"),
    path('admin_content/create', views.contentcreate, name="contentcreate"),
    path('admin_content/inserted', views.contentaddprocess, name="contentaddprocess"),
    path('admin_content/content_delete/<int:id>', views.contentdelete, name="contentdelete"),
    path('admin_content/content_edit/<int:id>', views.contentedit, name="contentedit"),
    path('admin_content/update', views.contentupdate, name="contentupdate"),

    path('AdminPayment/',views.AdminPaymentlisting,name='AdminPaymentlisting'),
     
    path('adminfeedback',views.feedbacklisting,name='feedbacklisting'),

    path('changepassword',views.changepassword,name='changepassword'),
    path('changepasswordprocess',views.changepasswordprocess,name='changepassword'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('forgotpasswordprocess',views.forgotpasswordprocess,name='forgotpassword'),
    path('upload',views.upload,name='upload'),
    

   
]
 

  




