from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages #import messages




# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='mental_health')
print('Successfully connected to database')
cur = conn.cursor()




def doctor_index(request):
    return render(request,'doctor/doctor_index.html')

def sidebar(request):
    return render(request,'doctor/sidebar.html')




#--------------------------------------------------Doctor event-----------------------------------------------------------------------------------------

def doctor_event(request):
    cur.execute('''SELECT
    `event_tbl`.`event_id`
    , `event_tbl`.`event_date`
    , `event_tbl`.`event_description`
    , `event_tbl`.`event_time`
    , `professional_tbl`.`professional_name`
    , `event_tbl`.`event_image`
    , `event_tbl`.`event_name`
FROM
    `event_tbl`
    INNER JOIN `professional_tbl` 
        ON (`event_tbl`.`mh_professional_id` = `professional_tbl`.`mh_professional_id`); ''')
    
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'doctor/doctor_event.html', {'events': data})  

#_________________________eventbooking________________________#
def doctor_event_booking(request):
    cur.execute(''' SELECT
    `event_booking`.`event_bookid`
    , `user_tbl`.`name`
    , `event_tbl`.`event_name`
    , `event_booking`.`user_mobile`
    , `event_booking`.`user_email`
FROM
    `user_tbl`
    INNER JOIN `event_booking` 
        ON (`user_tbl`.`user_id` = `event_booking`.`user_id`)
    INNER JOIN `event_tbl` 
        ON (`event_tbl`.`event_id` = `event_booking`.`event_id`); ''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'doctor/doctor_event_booking.html', {'events': data}) 
#_________________________doctorcontent___________________#


def doctor_content(request):
    cur.execute('''SELECT
    `content_tbl`.`content_id`
    , `content_typetbl`.`con_name`
    , `content_tbl`.`c_name`
    , `content_tbl`.`status`
    , `content_tbl`.`con_description`
    , `content_tbl`.`image`
    , `content_tbl`.`audio`
    , `content_tbl`.`video`
FROM
    `content_tbl`
    INNER JOIN `content_typetbl` 
        ON (`content_tbl`.`con_typeid` = `content_typetbl`.`con_typeid`);''')
    
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'doctor/doctor_content.html', {'contents': data})
#__________________contenttype________________________________#
def doctor_contenttype(request):
    cur.execute("SELECT * FROM `content_typetbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'doctor/doctor_contenttype.html', {'contents': data})   

    

def doctor_feedback(request):
    cur.execute('''SELECT
    `feedback_tbl`.`feedback_id`
    , `feedback_tbl`.`feedback_date`
    , `user_tbl`.`name`
    , `feedback_tbl`.`q1`
    , `feedback_tbl`.`q2`
    , `feedback_tbl`.`q3`
    , `feedback_tbl`.`q4`
    , `feedback_tbl`.`q5`
    , `feedback_tbl`.`q6`
    , `feedback_tbl`.`q7`
    , `feedback_tbl`.`q8`
    , `feedback_tbl`.`q9`
    FROM
    `feedback_tbl`
    INNER JOIN `user_tbl` 
        ON (`feedback_tbl`.`user_id` = `user_tbl`.`user_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'doctor/doctor_feedback.html', {'feedbacks': data})

def doctor_booking(request):
    cur.execute('''SELECT
    `book_tbl`.`book_id`
    , `book_tbl`.`book_time`
    , `user_tbl`.`name`
    , `professional_tbl`.`professional_name`
    , `book_tbl`.`book_question`
    , `book_tbl`.`user_mobile`
FROM
    `book_tbl`
    INNER JOIN `user_tbl` 
        ON (`book_tbl`.`user_id` = `user_tbl`.`user_id`)
    INNER JOIN `professional_tbl` 
        ON (`professional_tbl`.`mh_professional_id` = `book_tbl`.`mh_professional_id`);''')
   
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'doctor/doctor_booking.html', {'appts': data})




def doctor_forgot_password(request):
    return render(request,'doctor/doctor_forgot_password.html')


#---------------------------------------Change password-----------------------------------------------
def changepassword(request):
    return  render(request,'doctor/change_password.html')

def changepasswordprocess(request):
    if request.method == 'POST':
        if 'mh_professional_id' in request.COOKIES and request.session.has_key('mh_professional_id'):
            print(request.POST)
            mh_professional_id = request.session['mh_professional_id']
            opass = request.POST['current_pwd']
            npass = request.POST['new_pwd']
            cpass = request.POST['con_pwd']
            cur.execute("select * from `professional_tbl` where `mh_professional_id` = '{}'".format(mh_professional_id))
            db_data = cur.fetchone()
            if db_data is not None:
                if len(db_data) > 0:
                    #Fetch Data
                    oldpassword = db_data[7]
                    if opass == oldpassword:
                        if npass == cpass:
                            cur.execute("update  `professional_tbl` set `password` = {} where `mh_professional_id` = {}".format(npass,mh_professional_id))
                            conn.commit()
                            messages.success(request, 'Password Changed')
                            return render(request, 'doctor/doctor_index.html')
                        else:
                            messages.success(request, 'New and Confirm Password not Match')
                            return render(request, 'doctor/change_password.html')
                    else:
                        messages.success(request, 'Old Password not match')
                        return render(request, 'doctor/change_password.html')
                else:
                    messages.success(request, 'record not found ')
                    redirect(doctor_login) 
            else: 
                messages.success(request, 'Error ')
                redirect(doctor_login) 
        else:
            return redirect(doctor_login)
    else:
        return render(request, 'doctor/change_password.html') 



def doctor_profile(request):
    return render(request,'doctor/doctor_profile.html')
def register(request):
    return render(request,'doctor/doctor_register.html')
def registeraddprocess(request):
    
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['nm']
        email = request.POST['em']
        mobile = request.POST['cn']
       
        gender = request.POST['user_gender']
        pic = request.POST['img']
        cv = request.POST['cv']
       
        password = request.POST['pwd']
        
        cur.execute("INSERT INTO `professional_tbl`(`professional_name`,`email`,`contact_no`,`gender`,`pic`,`resume`,`password`) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(name,email,mobile,gender,pic,cv,password))
        conn.commit()
        messages.success(request, 'Registration Details added successfully')
   
        return redirect(register) 
    else:
        return redirect(register)

def edit_profile(request):
    return render(request,'doctor/edit_profile.html')

def profile(request):
    return render(request,'doctor/profile.html')


#--------------------------------------------Login------------------------------------------------------------------------------------------------


def doctor_index1(request):
    return render(request, 'doctor/doctor_index1.html')   

def doctor_login(request):
    if request.method == 'POST':
        print(request.POST)
        doctor_email = request.POST['e1']
        doctor_password = request.POST['password']
        cur.execute("select * from `professional_tbl` where `email` = '{}' and `password` = '{}'".format(doctor_email,doctor_password))
        data = cur.fetchone()
        
        if data is not None:

            if len(data) > 0:
                #Fetch Data
                doctor_db_id = data[0]
                doctor_db_email = data[3]
                print(doctor_db_id)
                print(doctor_db_email)
                #Session Create Code
                request.session['mh_professional_id'] = doctor_db_id
                request.session['doctor_email'] = doctor_db_email
                #Session Create Code
                #Cookie Code
                response = redirect(dashboard)
                response.set_cookie('mh_professional_id', doctor_db_id)
                response.set_cookie('doctor_email', doctor_db_email)
                return response
                #Cookie Code
            else:
                return render(request, 'doctor/doctor_login.html') 
        return render(request, 'doctor/doctor_login.html')
        
       # return redirect(dashboard) 
    else:
        return render(request, 'doctor/doctor_login.html') 

def dashboard(request):
    if 'doctor_email' in request.COOKIES and request.session.has_key('doctor_email'):
        
        doctor_emails = request.session['doctor_email']
        doctor_emailc = request.COOKIES['doctor_email']

        print("Session is  " + doctor_emails)
        print("Cookie is  " + doctor_emailc)

        return render(request, 'doctor/doctor_index.html')
    else:
        return redirect(doctor_login)


#---------------------------------------------Forgot Password---------------------------------------------------------------------------------------
def forgotpassword(request):
    return  render(request,'doctor/doctor_forgot_password.html')

    
def forgotpasswordprocess(request):
    print(request.POST)
    doctor_email = request.POST['forgot_email']
    cur.execute("select * from `professional_tbl` where `email` = '{}' ".format(doctor_email))
    db_data = cur.fetchone()
        
    if db_data is not None:
        if len(db_data) > 0:
            #Fetch Data
            doctor_db_id = db_data[0]
            doctor_db_email = db_data[3]
            doctor_db_password = db_data[11]
            print(doctor_db_id)
            print(doctor_db_email)
            
            subject = 'Forgot Password'
            message = ' Your Password is  ' + doctor_db_password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [doctor_db_email,]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Password Sent on Email ID')
            return redirect(doctor_login)
            #Cookie Code
        else:
            messages.success(request, 'Wrong Email Details')
            return render(request, 'doctor/doctor_forgot_password.html') 
    messages.success(request, 'Wrong Email Details')
    return render(request, 'doctor/doctor_forgot_password.html')
