from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core.files.storage import FileSystemStorage
          

from django.contrib import messages #import messages


# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='mental_health')
print('Successfully connected to database')
cur = conn.cursor()



def sidebar(request):
    return render(request,'admin/sidebar.html')


#--------------------------------------------------USER-----------------------------------------------------------------------------------------

def user(request):
    cur.execute("SELECT * FROM `user_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/user.html', {'users': data})   


#----------------------------------------------Change password--------------------------------------------------
def changepassword(request):
    return  render(request,'admin/change_password.html')

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
                            return render(request, 'admin/admin_index.html')
                        else:
                            messages.success(request, 'New and Confirm Password not Match')
                            return render(request, 'admin/change_password.html')
                    else:
                        messages.success(request, 'Old Password not match')
                        return render(request, 'admin/change_password.html')
                else:
                    messages.success(request, 'record not found ')
                    redirect(login) 
            else: 
                messages.success(request, 'Error ')
                redirect(login) 
        else:
            return redirect(login)
    else:
        return render(request, 'admin/change_password.html') 



def forgotpassword(request):
    return  render(request,'admin/forgot_password.html')

    
def forgotpasswordprocess(request):
    print(request.POST)
    professional_email = request.POST['forgot_email']
    cur.execute("select * from `professional_tbl` where `email` = '{}' ".format(professional_email))
    db_data = cur.fetchone()
        
    if db_data is not None:
        if len(db_data) > 0:
            #Fetch Data
            professional_db_id = db_data[0]
            professional_db_email = db_data[3]
            professional_db_password = db_data[11]
            print(professional_db_id)
            print(professional_db_email)
            
            subject = 'Forgot Password'
            message = ' Your Password is  ' + professional_db_password
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [professional_db_email,]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, 'Password Sent on Email ID')
            return redirect(login)
            #Cookie Code
        else:
            messages.success(request, 'Wrong Email Details')
            return render(request, 'admin/forgot_password.html') 
    messages.success(request, 'Wrong Email Details')
    return render(request, 'admin/forgot_password.html')



#--------------------------------------------------EVENT-----------------------------------------------------------------------------------------


def eventlisting(request):
    cur.execute('''SELECT
    `event_tbl`.`event_id`
    , `event_tbl`.`event_date`
    , `event_tbl`.`event_description`
    , `event_tbl`.`event_time`
    , `professional_tbl`.`professional_name`
    , `event_tbl`.`event_name`
  , `event_tbl`.`event_image`
    
FROM
    `event_tbl`
    INNER JOIN `professional_tbl` 
        ON (`event_tbl`.`mh_professional_id` = `professional_tbl`.`mh_professional_id`); ''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/admin_event.html', {'events': data})   

#def eventcreate(request):

 # return render(request, 'admin/event_add.html')   

def eventcreate(request):
    
    
    cur.execute("SELECT * FROM `user_tbl`")
    data1 = cur.fetchall()
    cur.execute("SELECT * FROM `professional_tbl`")
    data2 = cur.fetchall()

    #return list(data)
    print(list(data1)) 
    return render(request, 'admin/event_add.html',{'mydata': data1 ,'mydata2': data2,}) 

def eventaddprocess(request):
    messages.success(request, 'Event Details added successfully')
    if request.method == 'POST':
        print(request.POST)
       
        event_name = request.POST['event_name'] 
        event_description = request.POST['event_description']
        event_date = request.POST['event_date']
        event_time=request.POST['event_time']
        mh_professional_id = request.POST['mh_professional_id']
      
        
     
        cur.execute("INSERT INTO `event_tbl`(`event_name`,`event_description`,`event_date`,`event_time`,`mh_professional_id`) VALUES ('{}','{}','{}','{}','{}')".format(event_name,event_description,event_date,event_time,mh_professional_id))
        conn.commit()
       
        return redirect(eventcreate) 
    else:
       
        return redirect(eventcreate)



def eventdelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `event_tbl` where `event_id` = {}".format(id))
    conn.commit()
    return redirect(eventlisting) 


def eventedit(request,id):
     
    print(id)
    cur.execute("select * from `event_tbl` where `event_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/event_edit.html', {'events': data})   


def eventupdate(request):
    messages.success(request, 'Event Details updated successfully')
    
    if request.method == 'POST':
        print(request.POST)
        
        event_id = request.POST['event_id']
        event_name = request.POST['event_name']
        event_description = request.POST['event_description']
        event_date = request.POST['event_date']
        event_time=request.POST['event_time']
        professional_name = request.POST['professional_name']
       

       
        cur.execute("update `event_tbl` set `event_name`= '{}',`event_description`= '{}',`event_date`= '{}',`event_time`= '{}',`professional_name`= '{}' where `event_id`='{}'".format(event_name,event_description,event_date,event_time,professional_name,event_id))
        
        conn.commit()
        return redirect(eventlisting) 
    else:
        return redirect(eventlisting)

#---------------------------------------------EVENT BOOKING---------------------------------------------------------------------------------------------------------------
def eventbooklisting(request):
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
    return render(request, 'admin/admin_eventbook.html', {'ebook': data})   


def eventbookcreate(request):
    cur.execute("SELECT * FROM `user_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `event_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request, 'admin/eventbook_add.html',{'mydata':data,'mydata1':data1})   

   
def eventbookaddprocess(request):
    messages.success(request, 'Event  booking Details added successfully')
    if request.method == 'POST':
        print(request.POST)
       
       # event_bookid = request.POST['event_bookid']
       #Foreign key
        user_id = request.POST['user_id']
        event_id = request.POST['event_id']
       
        user_email = request.POST['user_email']
        user_number = request.POST['user_number']
        
 
        
     
        cur.execute("INSERT INTO `event_booking`(`user_id`,`user_email`,`user_mobile`,`event_id`) VALUES ('{}','{}','{}','{}')".format(user_id,user_email,user_number, event_id))
        conn.commit()
       
        return redirect(eventbookcreate) 
    else:
       
        return redirect(eventbookcreate)



def eventbookdelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `event_booking` where `event_bookid` = {}".format(id))
    conn.commit()
    return redirect(eventbooklisting) 


def eventbookedit(request,id):
     
    print(id)
    cur.execute("select * from `event_booking` where `event_bookid` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/eventbook_edit.html', {'ebooks': data})   


def eventbookupdate(request):
    messages.success(request, 'Event booking Details updated successfully')
    
    if request.method == 'POST':
        print(request.POST)
        
        event_bookid = request.POST['event_bookid']
        user_id = request.POST['user_id']
        user_email = request.POST['user_email']
        user_number = request.POST['user_number']
        event_id = request.POST['event_id']
       

       
        cur.execute("update `event_booking` set `user_id`= '{}',`user_email`= '{}',`user_mobile` = '{}' ,`event_id` = '{}' where `event_bookid`='{}'".format(user_id,user_email,user_number, event_id,event_bookid))
        
        conn.commit()
        return redirect(eventbooklisting) 
    else:
        return redirect(eventbooklisting)

#-------------------------------------------COMMUNITY DISCUSSION PAGE--------------------------------------------------------------------------

def cdplisting(request):
    cur.execute("select * from `community_tbl` ")
   
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/admincommques.html', {'cdp': data})   



def cdpdelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `community_tbl` where `communityque_id` = {}".format(id))
    conn.commit()
    return redirect(cdplisting) 

#-------------------------------------------COMMUNITY DISCUSSION PAGE ANSWER TABLE--------------------------------------------------------------------------

def cdpalisting(request):
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
    return render(request, 'admin/admincommans.html', {'cdpa': data})   



def cdpadelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `communityanswer_tbl` where `answer_id` = {}".format(id))
    conn.commit()
    return redirect(cdpalisting) 







#--------------------------------------------CONTENT TYPE-----------------------------------------------------------------------------------------

def contenttypelisting(request):
    cur.execute("SELECT * FROM `content_typetbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/admin_contenttype.html', {'ctypes': data})   

def contenttypecreate(request):
    return render(request, 'admin/contenttype_add.html')   

def contenttypeaddprocess(request):
    messages.success(request, 'content types Details added successfully')
   
    if request.method == 'POST':
        print(request.POST)
        con_name = request.POST['con_name']
        cur.execute("INSERT INTO `content_typetbl`(`con_name`) VALUES ('{}')".format(con_name))
        conn.commit()
        return redirect(contenttypecreate) 
    else:
        return redirect(contenttypecreate)


def contenttypedelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `content_typetbl` where `con_typeid` = {}".format(id))
    conn.commit()
    return redirect(contenttypelisting) 


def contenttypeedit(request,id):
     
    print(id)
    cur.execute("select * from `content_typetbl` where `con_typeid` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/contenttype_edit.html', {'ctypes': data})   


def contenttypeupdate(request):
    messages.success(request, 'content type Details updated successfully')
   
    if request.method == 'POST':
        print(request.POST)
        
        con_typeid = request.POST['con_typeid']
        con_name = request.POST['con_name']
       
        cur.execute("update `content_typetbl` set `con_name`= '{}' where `con_typeid`='{}'".format(con_name,con_typeid))
        conn.commit()
        return redirect(contenttypelisting) 
    else:
        return redirect(contenttypelisting)


#--------------------------------------------CONTENT-----------------------------------------------------------------------------------------

def contentlisting(request):
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
    return render(request, 'admin/admin_content.html', {'contents': data})   

def contentcreate(request):
    cur.execute("SELECT * FROM `professional_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
   
    cur.execute("SELECT * FROM `user_tbl`")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))

    cur.execute("SELECT * FROM `content_typetbl`")
    data2 = cur.fetchall()
    #return list(data)
    print(list(data2))
   
    return render(request, 'admin/content_add.html',{'mydata':data,'mydata1':data1,'mydata2':data2}) 
   
   

def contentaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        myfile = request.FILES['img']            
        fs = FileSystemStorage()
        filepath = "static/images/"
        filename = myfile.name
        fileupload = fs.save(filepath+myfile.name, myfile)
        uploaded_file_url = fs.url(fileupload)
        print(uploaded_file_url)
         #con_typeid = request.POST['ctid']
        c_name = request.POST['cn']
        
        status = request.POST['status']
        con_description = request.POST['desc']
       # image =request.POST['img']
        audio = request.POST['audio']
        video = request.POST['video']
        
        type = request.POST['type']
        
     
        cur.execute("INSERT INTO `content_tbl`(`c_name`,`con_description`,`image`,`audio`,`video`,`con_typeid`,`status`) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(c_name,con_description,myfile,audio,video,type,status))
        conn.commit()
        
        return redirect(contentcreate) 
    else:
        return redirect(contentcreate)

def contentdelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `content_tbl` where `content_id` = {}".format(id))
    conn.commit()
    return redirect(contentlisting) 


def contentedit(request,id):
    
    print(id)
    cur.execute("select * from `content_tbl` where `content_id` = {}".format(id))
    
    data = cur.fetchone()
    cur.execute("SELECT * FROM `content_typetbl`")
   
    #return list(data)
    print(list(data))
    return render(request, 'admin/content_edit.html')   


def contentupdate(request):
   
    messages.success(request, 'content  Details updated successfully')
   
    if request.method == 'POST':
        print(request.POST)
        content_id = request.POST['ctid']
        c_name = request.POST['cn']
        status = request.POST['status']
        con_description = request.POST['desc']
        image =request.POST['img']
        audio = request.POST['audio']
        video = request.POST['video']
        
      #  type = request.POST['type']
        

         
        cur.execute("update `content_tbl` set  `c_name`= '{}',`con_description`= '{}',`image`= '{}',`audio`= '{}',`video` = '{}',`status`={} where `content_id`= '{}' ".format(c_name,con_description,image,audio,video,status,content_id))
   
        conn.commit()
        return redirect(contentlisting) 
    else:
        return redirect(contentlisting)




#---------------------------------------------------------------------------------Professional----------------------------------------------------
def professionallisting(request):
    cur.execute("SELECT * FROM `professional_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/adminprofessional.html', {'pros': data}) 


def professionalcreate(request):
    return render(request, 'admin/professional_add.html')   

def professionaladdprocess(request):
    messages.success(request, 'professional Details added successfully')
   
    if request.method == 'POST':
        print(request.POST)
        professional_name = request.POST['fn1']
        type = request.POST['type']
        email = request.POST['em']
        contact = request.POST['cn1']
        gender = request.POST['user_gender']
        description = request.POST['doc_desc']
        pic = request.POST['pic']
        resume = request.POST['resume']
        active = request.POST['active']
        charges = request.POST['ch']
        date = request.POST['date']
        
        cur.execute("INSERT INTO `professional_tbl`(`professional_name`,`type`,`email`,`contact_no`,`gender`,`description`,`pic`,`resume`,`charges`,`active`,`joining_date`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(professional_name,type,email,contact,gender,description,pic,resume,charges,active,date))
        conn.commit()
        return redirect(professionalcreate) 
    else:
        return redirect(professionalcreate)

    
def professionaldelete(request,id):
     
   #id = request.GET['id']
    #id = User.objects.get(id=id)
   print(id)
   cur.execute("delete from `professional_tbl` where `mh_professional_id` = {}".format(id))
   conn.commit()
   return redirect(professionallisting) 



def professionaledit(request,id):
     
    print(id)
    cur.execute("select * from `professional_tbl` where `mh_professional_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/professional_edit.html/', {'pros': data})   


def professionalupdate(request):
    messages.success(request, 'professional Details updated successfully')
   
    if request.method == 'POST':
        print(request.POST)

        mh_professional_id = request.POST['proid']
        professional_name = request.POST['fn1']
        type = request.POST['type']
        email = request.POST['em']
        contact = request.POST['cn1']
        gender = request.POST['user_gender']
        description = request.POST['doc_desc']
        pic = request.POST['pic']
        resume = request.POST['resume']
        active = request.POST['active']
        charges = request.POST['ch']
        date = request.POST['date']
        

        cur.execute("update `professional_tbl` set  `professional_name` = '{}',`type` = '{}',`email` = '{}',`contact_no` = '{}',`gender` = '{}' ,`description` = '{}',`charges` = '{}',`pic` = '{}',`resume` = '{}', `joining_date` = '{}'  where `mh_professional_id`='{}'".format(professional_name,type,email,contact,gender,description,charges,pic,resume,active,date, mh_professional_id))
        conn.commit()
        return redirect(professionallisting) 
    else:
        return redirect(professionallisting)

#--------------------------------Admin Self Assesment Test--------------------------------------------------------------------------------------
def testlisting(request):
    cur.execute("SELECT * FROM `test_tbl`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/admin_testque.html', {'tests': data})   

def testcreate(request):
    return render(request, 'admin/test_add.html')   

def testaddprocess(request):
    messages.success(request, 'Tests Details added successfully')
   
    if request.method == 'POST':
        print(request.POST)
        test_question = request.POST['tq']
        option1 = request.POST['o1']
        option2 = request.POST['o2']
        option3 = request.POST['o3']
        option4 = request.POST['o4']
        option1_marks = request.POST['om1']
        option2_marks = request.POST['om2']
        option3_marks = request.POST['om3']
        option4_marks = request.POST['om4']
        
        
        cur.execute("INSERT INTO `test_tbl`(`test_question`,`option1`,`option2`,`option3`,`option4`,`option1_marks`,`option2_marks`,`option3_marks`,`option4_marks`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(test_question,option1,option2,option3,option4,option1_marks,option2_marks,option3_marks,option4_marks))
        conn.commit()
        return redirect(testcreate) 
    else:
        return redirect(testcreate)


def testdelete(request,id):
     
   #id = request.GET['event_id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `test_tbl` where `test_questionid` = {}".format(id))
    conn.commit()
    return redirect(testlisting) 


def testedit(request,id):
     
    print(id)
    cur.execute("select * from `test_tbl` where `test_questionid` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/test_edit.html', {'tests': data})   


def testupdate(request):
    messages.success(request, 'Test Details updated successfully')
   
    if request.method == 'POST':
        print(request.POST)
        
        test_questionid = request.POST['tid']
        test_question = request.POST['tq']
        option1 = request.POST['o1']
        option2 = request.POST['o2']
        option3 = request.POST['o3']
        option4 = request.POST['o4']
        option1_marks = request.POST['om1']
        option2_marks = request.POST['om2']
        option3_marks = request.POST['om3']
        option4_marks = request.POST['om4']
      
        
        cur.execute("update `test_tbl` set `test_question`= '{}',`option1`= '{}',`option2`= '{}',`option3`= '{}',`option4`= '{}',`option1_marks`= '{}',`option2_marks`= '{}',`option3_marks`= '{}',`option4_marks`= '{}'  where `test_questionid`='{}'".format(test_question,option1,option2,option3,option4,option1_marks,option2_marks,option3_marks,option4_marks,test_questionid))
        conn.commit()
        return redirect(testlisting) 
    else:
        return redirect(testlisting)


#________________________self aseesment test answer---------------------------

def testanswerlisting(request):
    cur.execute('''SELECT
    `testuserans_tbl_1`.`Testuserans_id`
    , `testuserans_tbl_1`.`User_Option`
    , `user_tbl`.`name`
    , `test_tbl`.`test_question`
FROM
    `test_tbl`
    INNER JOIN `testuserans_tbl` AS `testuserans_tbl_1` 
        ON (`test_tbl`.`test_questionid` = `testuserans_tbl_1`.`Test_queid`)
    INNER JOIN `user_tbl` 
        ON (`user_tbl`.`user_id` = `testuserans_tbl_1`.`User_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/admin_testanswer.html', {'tests': data})   


#--------------------------------Admin Payment------------------------




def AdminPaymentlisting(request):
    cur.execute('''SELECT
    `payment_tbl`.`payment_id`
    , `book_tbl`.`book_id`
    , `payment_tbl`.`payment_mode`
    , `payment_tbl`.`payment_date`
    , `payment_tbl`.`payment_status`
    , `user_tbl`.`name`
    , `book_tbl`.`charges`
FROM
    `book_tbl`
    INNER JOIN `payment_tbl` 
        ON (`book_tbl`.`book_id` = `payment_tbl`.`book_id`)
    INNER JOIN `user_tbl` 
        ON (`payment_tbl`.`user_id` = `user_tbl`.`user_id`);''')
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'admin/AdminPayment.html', {'payment': data})   


#--------------------------------Admin Feedback------------------------#
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
    return render(request, 'admin/adminfeedback.html', {'fbs': data})   

#---------------------------login--------------------------------------------#
def admin_index(request):
    return render(request, 'admin/admin_index.html')   

def login(request):
    if request.method == 'POST':
        print(request.POST)
        admin_email = request.POST['e1']
        admin_password = request.POST['password']
        cur.execute("select * from `user_tbl` where `email` = '{}' and `password` = '{}'".format(admin_email,admin_password))
        data = cur.fetchone()
        
        if data is not None:

            if len(data) > 0:
                #Fetch Data
                admin_db_id = data[0]
                admin_db_email = data[3]
                print(admin_db_id)
                print(admin_db_email)
                #Session Create Code
                request.session['admin_id'] = admin_db_id
                request.session['admin_email'] = admin_db_email
                #Session Create Code
                #Cookie Code
                response = redirect(dashboard)
                response.set_cookie('admin_id', admin_db_id)
                response.set_cookie('admin_email', admin_db_email)
                return response
                #Cookie Code
            else:
                return render(request, 'admin/admin_login.html') 
        return render(request, 'admin/admin_login.html')
        
       # return redirect(dashboard) 
    else:
        return render(request, 'admin/admin_login.html') 

def dashboard(request):
    if 'admin_email' in request.COOKIES and request.session.has_key('admin_email'):
        
        admin_emails = request.session['admin_email']
        admin_emailc = request.COOKIES['admin_email']

        print("Session is  " + admin_emails)
        print("Cookie is  " + admin_emailc)

        return render(request, 'admin/admin_index.html')
    else:
        return redirect(login)




def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'admin/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'admin/upload.html')













