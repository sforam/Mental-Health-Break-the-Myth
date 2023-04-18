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



# Create your views here.

def sidebaruserpanel(request):
    return render(request,'user/sidebaruserpanel.html')

def index3(request):
    return render(request,'user/index3.html') 
def index3(request):
    return render(request,'user/index3.html')
def expert1(request):
    cur.execute("select * from `professional_tbl` where type = 'expert'")
    data = cur.fetchall()
    print(data)
    return render(request,'user/expert1.html',{'mydata':data})
def change_password(request):
    return render(request,'user/change_password.html')
def videos(request):
    return render(request,'user/videos.html')
def resources(request):
    return render(request,'user/resources.html')
def Grief(request):
    return render(request,'user/Grief.html')
def Addiction(request):
    return render(request,'user/Addiction.html')
def Anxiety(request):
    return render(request,'user/Anxiety.html')
def Depression(request):
    return render(request,'user/Depression.html')
def MoodDisorder(request):
    return render(request,'user/MoodDisorder.html')
def EatingDisorder(request):
    return render(request,'user/EatingDisorder.html')
def Stress(request):
    return render(request,'user/Stress.html')
def SleepDisturbances(request):
    return render(request,'user/SleepDisturbances.html')



def soumya(request):
    return render(request,'user/soumya.html')
def doctor1(request):
    return render(request,'user/doctor1.html')

def event(request):
    cur.execute("select * from `event_tbl`")
    data = cur.fetchall()
    print(data)
    return render(request,'user/event.html',{'mydata':data})

def connect(request):
    cur.execute("SELECT * FROM `user_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `event_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request, 'user/connect.html',{'mydata':data,'mydata1':data1})   

    
def connectaddprocess(request):
    messages.success(request, 'Events Details Sent successfully')
    if request.method == 'POST':
        print(request.POST)
        user = request.POST['nm']
        email = request.POST['email']
        mobile = request.POST['phone']
        book_name=request.POST['book_name']
       
        
        cur.execute("INSERT INTO `event_booking`(`user_id`,`event_id`,`user_email`,`user_mobile`) VALUES ('{}','{}','{}','{}')".format(user,book_name,email,mobile))
        conn.commit()
        return redirect(connect) 
    else:
        return redirect(connect)



def eventdetails(request,id):
    cur.execute("select * from `event_tbl` where `event_id` = {}".format(id))
    data = cur.fetchone()
    return render(request,'user/eventdetails.html',{'data':data})


def selfassessment1_test(request):
    return render(request,'user/selfassessment1_test.html')
def selfassessment1_testaddprocess(request):
    messages.success(request, 'Test Details Send successfully')
    if request.method == 'POST':
        print(request.POST)
        user_option = request.POST['q1']
        user_option2 = request.POST['q2']
        user_option3 = request.POST['q3']
        user_option4 = request.POST['q4']
        user_option5 = request.POST['q5']
        user_option6 = request.POST['q6']
        user_option7 = request.POST['q7']
        user_option8 = request.POST['q8']
        user_option9 = request.POST['q9']
        user_option10 = request.POST['q10']
       
       
       
       
       
       
       
       
       
        user_id = request.COOKIES['user_id']

        qid = request.POST['qid1']
        qid2 = request.POST['qid2']
        qid3 = request.POST['qid3']
        qid4 = request.POST['qid4']
        qid5 = request.POST['qid5']
        qid6 = request.POST['qid6']
        qid7 = request.POST['qid7']
        qid8 = request.POST['qid8']
        qid9 = request.POST['qid9']
        qid10 = request.POST['qid10']
        
       
        
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option,user_id,qid))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option2,user_id,qid2))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option3,user_id,qid3))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option4,user_id,qid4))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option5,user_id,qid5))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option6,user_id,qid6))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option7,user_id,qid7))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option8,user_id,qid8))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option9,user_id,qid9))
        cur.execute("INSERT INTO `testuserans_tbl`(`user_option`,`user_id`,`Test_queid`) VALUES ('{}','{}','{}')".format(user_option10,user_id,qid10))
       
        conn.commit()
        return redirect(selfassessment1_test) 
    else:
        return redirect(selfassessment1_test)


def result(request):
    cur.execute(''' SELECT
    SUM(`User_Option`)
    , `User_id`
    FROM
    `testuserans_tbl`
    GROUP BY `User_id`''')
    data = cur.fetchall()
    
    return render(request,'user/result.html',{'data':data})
    

 
def event4(request):
    return render(request,'user/event4.html')
def whatismentalhealth(request):
    return render(request,'user/whatismentalhealth.html')
def event3(request):
    return render(request,'user/event3.html')
def event2(request):
    return render(request,'user/event2.html')
def cdp(request):
    cur.execute('''select * from `community_tbl` where community_group="Addiction Support" ORDER BY "postdate_time" Asc''')
    data = cur.fetchall()
    print(data)
    
    cur.execute('''select * from `community_tbl` where community_group="Living With Depression"''')
    data1 = cur.fetchall()
    print(data1)
    
    return render(request,'user/cdp.html',{'mydata':data,'mydata1':data1,})

    
def cdpaddprocess(request):
    
    if request.method == 'POST':
        print(request.POST)
        q1 = request.POST['question1']
        q2 = request.POST['question2']
         
        
        
        cur.execute("INSERT INTO `community_tbl`(`community_ques`) VALUES ('{}')".format(q1))
        cur.execute("INSERT INTO `community_tbl`(`community_ques`) VALUES ('{}')".format(q2))
        
        conn.commit()
        return redirect(cdp) 
    else:
        return redirect(cdp)

def feedback(request):
    return render(request,'user/feedback.html')
def feedbackaddprocess(request):
    messages.success(request, 'Feedback Details Sent successfully')
    if request.method == 'POST':
        print(request.POST)
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        q6 = request.POST['q6']
        q7 = request.POST['q7']
        q8 = request.POST['q8']
        q9 = request.POST['q9']
        
        
        cur.execute("INSERT INTO `feedback_tbl`(`q1`,`q2`,`q3`,`q4`,`q5`,`q6`,`q7`,`q8`,`q9`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(q1,q2,q3,q4,q5,q6,q7,q8,q9))
        conn.commit()
        return redirect(feedback) 
    else:
        return redirect(feedback)

def viewfeedback(request):
    print(id)
    cur.execute("select * from `feedback_tbl`")
    data = cur.fetchone()
  
    return render(request,'user/viewfeedback.html', {'feedbacks': data}) 

def book_expert(request,id):
    print(id)
    cur.execute("select * from `professional_tbl` where `mh_professional_id` = {}".format(id))
    data = cur.fetchone()
  
    return render(request,'user/book_expert_bhoomika.html', {'experts': data}) 

def expertdetails(request,id):
    cur.execute("select * from `professional_tbl` where `mh_professional_id` = {}".format(id))
    data = cur.fetchone()
    return render(request,'user/expertdetails.html',{'data':data})

def book_doctor(request,id):
    print(id)
    cur.execute("select * from `professional_tbl` where `mh_professional_id` = {}".format(id))
    data = cur.fetchone()
  
    return render(request,'user/book_doctor_nitish.html', {'doctors': data}) 

def doctordetails(request,id):
    cur.execute("select * from `professional_tbl` where `mh_professional_id` = {}".format(id))
    data = cur.fetchone()
    return render(request,'user/doctordetails.html',{'data':data})



def book_doctor_nitishaddprocess(request):
   
    if request.method == 'POST':
        print(request.POST)
        bookdatetime = request.POST['dt']
        Counsellingquestion = request.POST['cq']
        mobile = request.POST['mobnum']
       
        
        
        cur.execute("INSERT INTO `book_tbl`(`book_time`,`book_question`,`user_mobile`) VALUES ('{}','{}','{}')".format(bookdatetime, Counsellingquestion,mobile))
        conn.commit()
        messages.success(request, ' Doctor Booking Session  Confirmed')
   
        return redirect(paymentpage2) 
    else:
        return redirect(book_doctor)



def book_expert_bhoomikaaddprocess(request):
   
    if request.method == 'POST':
        print(request.POST)
        mid=request.POST['mhid']
        user_id = request.COOKIES['user_id']
        bookdatetime = request.POST['dt']
        Counsellingquestion = request.POST['cq']
        mobile = request.POST['mobnum']
        payment_mode=request.POST['payment_method1']
        payment_amount=request.POST['pa']
        cur.execute("INSERT INTO `book_tbl`(`book_time`,`user_id`,`mh_professional_id`,`book_question`,`user_mobile`,`charges`) VALUES ('{}','{}','{}','{}','{}','{}')".format(bookdatetime,user_id,mid, Counsellingquestion,mobile,payment_amount))
        conn.commit()
        bookid = cur.lastrowid
        print(bookid)
        cur.execute("INSERT INTO `payment_tbl`(`user_id`,`payment_mode`,`payment_amount`,`book_id`) VALUES ('{}','{}','{}','{}')".format(user_id,payment_mode,payment_amount,bookid))
        conn.commit()

        messages.success(request, ' Exprert Booking Session  Confirmed')
        return redirect(paymentpage1) 
    else:
        return redirect(book_expert)


def selfassessment2_test(request):
    return render(request,'user/selfassessment2_test.html')
def doctor(request):
    return render(request,'user/doctor.html')
def nitish(request):
    return render(request,'user/nitish.html')
def book(request):
    return render(request,'user/book.html')
#----------------------------------------------------------------REGISTRATION----------------------------------------------------------------
def register1(request):
    return render(request,'user/register1.html')
def registeraddprocess(request):
    
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['nm']
        email = request.POST['em']
        mobile = request.POST['cn']
       
        gender = request.POST['user_gender']
        password = request.POST['pwd']
        
        cur.execute("INSERT INTO `user_tbl`(`name`,`email`,`contact_no`,`gender`,`password`) VALUES ('{}','{}','{}','{}','{}')".format(name,email,mobile,gender,password))
        conn.commit()
        messages.success(request, 'Registration Details added successfully')
   
        return redirect(register1) 
    else:
        return redirect(register1)


def login1(request):
    return render(request,'user/login1.html')
def book2(request):
    return render(request,'user/book2.html')
def doctor1(request):
    cur.execute("select * from `professional_tbl` where type = 'doctor'")
    data = cur.fetchall()
    print(data)
    return render(request,'user/doctor1.html',{'mydata':data})
def forgot_password(request):
    return render(request,'user/forgot_password.html')
def book_doctor_nitish(request):
    return render(request,'user/book_doctor_nitish.html')


def login(request):
    if request.method == 'POST':
        print(request.POST)
        user1_email = request.POST['login1_email']
        user1_password = request.POST['login_password']
        cur.execute("select * from `user_tbl` where `email` = '{}' and `password` = '{}'".format(user1_email,user1_password))
        data = cur.fetchone()
        
        if data is not None:

            if len(data) > 0:
                #Fetch Data
                user_db_id = data[0]
                user_db_email = data[2]
                print(user_db_id)
                print(user_db_email)
                #Session Create Code
                request.session['user_id'] = user_db_id
                request.session['user_email'] = user_db_email
                #Session Create Code
                #Cookie Code
                response = redirect(dashboard)
                response.set_cookie('user_id', user_db_id)
                response.set_cookie('user_email', user_db_email)
                return response
                #Cookie Code
            else:
                return render(request, 'user/login1.html') 
        return render(request, 'user/login1.html')
        
       # return redirect(dashboard) 
    else:
        return render(request, 'user/login1.html') 

def dashboard(request):
    if 'user_email' in request.COOKIES and request.session.has_key('user_email'):
        
        user_emails = request.session['user_email']
        user_emailc = request.COOKIES['user_email']

        print("Session is  " + user_emails)
        print("Cookie is  " + user_emailc)

        return render(request, 'user/index3.html')
    else:
        return redirect(login)


def changepassword(request):
    return  render(request,'user/change_password.html')

def changepasswordprocess(request):
    if request.method == 'POST':
        if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
            print(request.POST)
            user_id = request.session['user_id']
            opass = request.POST['current_pwd']
            npass = request.POST['new_pwd']
            cpass = request.POST['con_pwd']
            cur.execute("select * from `user_tbl` where `user_id` = '{}'".format(user_id))
            db_data = cur.fetchone()
            if db_data is not None:
                if len(db_data) > 0:
                    #Fetch Data
                    oldpassword = db_data[7]
                    if opass == oldpassword:
                        if npass == cpass:
                            cur.execute("update  `user_tbl` set `password` = {} where `user_id` = {}".format(npass,user_id))
                            conn.commit()
                            messages.success(request, 'Password Changed')
                            return render(request, 'user/index3.html')
                        else:
                            messages.success(request, 'New and Confirm Password not Match')
                            return render(request, 'user/change_password.html')
                    else:
                        messages.success(request, 'Old Password not match')
                        return render(request, 'user/change_password.html')
                else:
                    messages.success(request, 'record not found ')
                    redirect(login) 
            else: 
                messages.success(request, 'Error ')
                redirect(login) 
        else:
            return redirect(login)
    else:
        return render(request, 'user/change_password.html') 




def forgotpassword(request):
    return  render(request,'user/forgot-password.html')

    
def forgotpasswordprocess(request):
    print(request.POST)
    user_email = request.POST['forgot_email']
    cur.execute("select * from `user_tbl` where `email` = '{}' ".format(user_email))
    db_data = cur.fetchone()
        
    if db_data is not None:
        if len(db_data) > 0:
            #Fetch Data
            user_db_id = db_data[0]
            user_db_email = db_data[3]
            user_db_password = db_data[7]
            print(user_db_id)
            print(user_db_email)
            
            subject = 'Forgot Password'
            message = ' Your Password is  ' + user_db_password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user_db_email,]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Password Sent on Email ID')
            return redirect(login)
            #Cookie Code
        else:
            messages.success(request, 'Wrong Email Details')
            return render(request, 'user/forgot_password.html') 
    messages.success(request, 'Wrong Email Details')
    return render(request, 'user/forgot_password.html')
def paymentpage1(request):
    return render(request,'user/paymentpage1.html')
def paymentpage2(request):
    return render(request,'user/paymentpage2.html')