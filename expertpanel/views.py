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



def register(request):
    return render(request,'expert/expert_register.html')
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


#--------------------------------------------Login------------------------------------------------------------------------------------------------


def expert_index1(request):
    return render(request, 'expert/expert_index1.html')   

def expert_login(request):
    if request.method == 'POST':
        print(request.POST)
        expert_email = request.POST['e1']
        expert_password = request.POST['password']
        cur.execute("select * from `professional_tbl` where `email` = '{}' and `password` = '{}'".format(expert_email,expert_password))
        data = cur.fetchone()
        
        if data is not None:

            if len(data) > 0:
                #Fetch Data
                expert_db_id = data[0]
                expert_db_email = data[3]
                print(expert_db_id)
                print(expert_db_email)
                #Session Create Code
                request.session['mh_professional_id'] = expert_db_id
                request.session['expert_email'] = expert_db_email
                #Session Create Code
                #Cookie Code
                response = redirect(dashboard)
                response.set_cookie('mh_professional_id', expert_db_id)
                response.set_cookie('expert_email', expert_db_email)
                return response
                #Cookie Code
            else:
                return render(request, 'expert/expert_login.html') 
        return render(request, 'expert/expert_login.html')
        
       # return redirect(dashboard) 
    else:
        return render(request, 'expert/expert_login.html') 

def dashboard(request):
    if 'expert_email' in request.COOKIES and request.session.has_key('expert_email'):
        
        expert_emails = request.session['expert_email']
        expert_emailc = request.COOKIES['expert_email']

        print("Session is  " + expert_emails)
        print("Cookie is  " + expert_emailc)

        return render(request, 'expert/expert_index.html')
    else:
        return redirect(expert_login)





def expert_index(request):
    return render(request,'expert/expert_index.html')
def sidebar(request):
    return render(request,'expert/sidebar.html')

def profile(request):
    return render(request,'expert/profile.html')



def booklisting(request):
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
    return render(request, 'expert/book.html', {'books': data}) 

def bookedit(request,id):
     
    print(id)
    cur.execute("select * from `book_tbl` where `book_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'expert/book_edit.html', {'books': data})   

def bookdelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `book_tbl` where `book_id` = {}".format(id))
    conn.commit()
    return redirect(booklisting) 




def bookupdate(request):
    messages.success(request, 'Books Details updated successfully')
   
    if request.method == 'POST':
        print(request.POST)
        
        book_id = request.POST['book_id']
        btime= request.POST['bt']

        userid=request.POST['uid']
        proid=request.POST['proid']
        bquestion=request.POST['bq']

        mobile=request.POST['mb']

        cur.execute("update `book_tbl` set `book_time`= '{}',`user_id`= '{}',`mh_professional_id`= '{}',`book_question`= '{}',`user_mobile`= '{}' where `book_id`='{}'".format(btime,userid,proid,bquestion,mobile,book_id))
        conn.commit()
        
        return redirect(booklisting) 
    else:
        return redirect(booklisting)





def com_answerlisting(request):
    cur.execute('''SELECT
    `communityanswer_tbl`.`answer_id`
    , `community_tbl`.`community_ques`
    , `communityanswer_tbl`.`community_ans`
    , `communityanswer_tbl`.`apost_date`
    , `communityanswer_tbl`.`community_group`
    , `user_tbl`.`name`
    , `professional_tbl`.`professional_name`
FROM
    `communityanswer_tbl`
    INNER JOIN `user_tbl` 
        ON (`communityanswer_tbl`.`user_id` = `user_tbl`.`user_id`)
    INNER JOIN `professional_tbl` 
        ON (`communityanswer_tbl`.`mh_professional_id` = `professional_tbl`.`mh_professional_id`)
    INNER JOIN `community_tbl` 
        ON (`community_tbl`.`communityque_id` = `communityanswer_tbl`.`communityque_id`);''')
  
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'expert/com_answer.html', {'comans': data}) 

    
def com_answercreate(request):
    
    

    cur.execute("SELECT * FROM `user_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))

    cur.execute("SELECT * FROM `professional_tbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))

    cur.execute("SELECT * FROM `community_tbl`")
    data3 = cur.fetchall()
    #return list(data)
    print(list(data3))
   
   
    return render(request, 'expert/com_answer_add.html', {'mydata1':data1,'mydata2':data2,'mydata3':data3})

def com_answeraddprocess(request):
    messages.success(request, 'Answer Details added successfully')
   
    if request.method == 'POST':
        print(request.POST)
        commqueid = request.POST['cqi']
        com_ans = request.POST['ca']
        apsotdate= request.POST['apd']
        comgrp = request.POST['cg']
        user_id = request.POST['uid']
        professional_id = request.POST['proid']
        
        cur.execute("INSERT INTO `communityanswer_tbl`(`commqueid`,`com_ans`,`apsotdate`,` comgrp`,`user_id`,` professional_id`) VALUES ('{}','{}','{}','{}','{}','{}')".format(commqueid,com_ans,apsotdate,comgrp,user_id,professional_id))
        conn.commit()
        return redirect(com_answercreate) 
    else:
        return redirect(com_answercreate)

    

def com_answerdelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `communityanswer_tbl` where `answer_id` = {}".format(id))
    conn.commit()
    return redirect(com_answerlisting) 
 
def edit_profile(request):
    return render(request,'expert/edit_profile.html')

def com_queslisting(request):
    cur.execute("select * from `community_tbl` ")
   
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'expert/com_ques.html', {'comques': data})   
 
    

#---------------------------------------------Forgot Password---------------------------------------------------------------------------------------
def forgotpassword(request):
    return  render(request,'expert/expert_forgot_pwd.html')

    
def forgotpasswordprocess(request):
    print(request.POST)
    expert_email = request.POST['forgot_email']
    cur.execute("select * from `professional_tbl` where `email` = '{}' ".format(expert_email))
    db_data = cur.fetchone()
        
    if db_data is not None:
        if len(db_data) > 0:
            #Fetch Data
            expert_db_id = db_data[0]
            expert_db_email = db_data[3]
            expert_db_password = db_data[11]
            print(expert_db_id)
            print(expert_db_email)
            
            subject = 'Forgot Password'
            message = ' Your Password is  ' + expert_db_password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [expert_db_email,]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Password Sent on Email ID')
            return redirect(expert_login)
            #Cookie Code
        else:
            messages.success(request, 'Wrong Email Details')
            return render(request, 'expert/expert_forgot_pwd.html') 
    messages.success(request, 'Wrong Email Details')
    return render(request, 'expert/expert_forgot_pwd.html')

#---------------------------------------Change password-----------------------------------------------
def changepassword(request):
    return  render(request,'expert/change_password.html')

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
                            return render(request, 'expert/expert_index.html')
                        else:
                            messages.success(request, 'New and Confirm Password not Match')
                            return render(request, 'expert/change_password.html')
                    else:
                        messages.success(request, 'Old Password not match')
                        return render(request, 'expert/change_password.html')
                else:
                    messages.success(request, 'record not found ')
                    redirect(expert_login) 
            else: 
                messages.success(request, 'Error ')
                redirect(expert_login) 
        else:
            return redirect(expert_login)
    else:
        return render(request, 'expert/change_password.html') 



def expert_index1(request):
    return render(request,'expert/expert_index1.html')
def expert_login(request):
    return render(request,'expert/expert_login.html')
def feedbacklisting(request):
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
    return render(request, 'expert/feedback.html', {'feedback': data}) 


def logout(request):
    return render(request,'expert/logout.html')