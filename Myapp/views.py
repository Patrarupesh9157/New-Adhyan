import datetime
from tempfile import tempdir
from venv import create
from django.shortcuts import redirect, render
from .models import *
import random as r
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    uid=Register.objects.get(email=request.session['email'])
    return render(request,'index.html',{'uid':uid})
def login(request):
    try:
        uid=Register.objects.get(email=request.session['email'])
        return redirect('index')
    except:
        # global nowtime
        if request.method=='POST':
            try:
                uid=Register.objects.get(email=request.POST['email'])
                if uid.password==request.POST['password']:
                    request.session['email']=uid.email
                    # nowtime=datetime.datetime.now()
                    return redirect('index')
                return render(request,'login.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'register.html',{'msg':'Email is not registered'})
        return render(request,'login.html')
def register(request):
    if request.method=='POST':
        try:
            Register.objects.get(email=request.POST['email'])
            return render(request,'register.html',{'msg':'Email is alrady register.'})
        except:
            if request.POST['password']==request.POST['cpassword']:
                global temp
                temp={
                    'name':request.POST['name'],
                    'mobile':request.POST['mobile'],
                    'gender':request.POST['gender'],
                    'email':request.POST['email'],
                    'address':request.POST['address'],
                    'password':request.POST['password'],
                }
                otp = r.randrange(100000,999999)
                subject = 'welcome to Adhyan.'
                message = f'Your otp is {otp} .Please Enter valid Otp'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'otp.html',{'otp':otp})
            return render(request,'register.html',{'msg':'Both passwords are not matched'})
    return render(request,'register.html')
def otp(request):
    if request.method=='POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            Register.objects.create(
                name=temp['name'],
                mobile=temp['mobile'],
                gender=temp['gender'],
                email=temp['email'],
                address=temp['address'],
                password=temp['password']
            )
            msg='Account is Created'
            return render(request,'login.html',{'msg': msg})
        return render(request,'otp.html',{'otp':request.POST['otp'],'msg':'incorrect OTP'})
def logout(request):
    del request.session['email']
    return redirect('login')

def forgot(request):
    if request.method=='POST':
        uid=Register.objects.get(email=request.POST['email'])
        if uid.email==request.POST['email']:
            fpass = r.randrange(100000,999999)
            subject = 'Forgot Password For Adhyan Id'
            message = f'Your new Password is {fpass} .Please Enter This Password for Login'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'fpass.html',{'fpass':fpass,'Email':uid.email,'msg':'See in Your Email id Your Password is Sent'})
        return render(request,'forgot-password.html',{'msg':'Email Is not Register'})
    return render(request,'forgot-password.html')


def passwordrecovery(request):
    uid=Register.objects.get(email=request.session['email'])
    if request.method=='POST':
        if uid.password == request.POST['opassword']:
            if request.POST['npassword'] == request.POST['cpassword']:
                uid.password = request.POST['npassword']
                uid.save()
                return redirect('index')
            return render(request,'password-recovery.html',{'msg':'Both Password Are not Matched '})
        return render(request,'password-recovery.html',{'msg':'Old Password is not Matched '})
    return render(request,'password-recovery.html')

def fpass(request):
    try:
        uid=Register.objects.get(email=request.session['email'])
        return redirect('index')
    except:
        if request.method=='POST':
            try:
                uid=Register.objects.get(email=request.POST['email'])
                if request.POST['password']==request.POST['fpass']:
                    uid.password=request.POST['fpass']
                    uid.save()
                    request.session['email']=uid.email
                    return redirect('index')
                return render(request,'fpass.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'register.html',{'msg':'Email is not registered'})
        return render(request,'fpass.html')

def addcourse(request):
    uid=Register.objects.get(email=request.session['email'])
    if request.method=='POST':
        try:
            course=All_Course.objects.get(coname=request.POST['coname'])
            msg = f'Course is already in list and status is'
            return render(request,'add-course.html',{'uid':uid,'msg':msg})
        except:   
            All_Course.objects.create(
                uid = uid,
                coname=request.POST['coname'],
                coduration=request.POST['coduration'],
                coprice=request.POST['coprice'],
                codepartment=request.POST['codepartment'],
                copic=request.FILES['copic'],
                codiscription=request.POST['codiscription'],
                coyear=request.POST['coyear'],
            )
            msg = 'Course added and waiting for Approvel'
            return render(request,'add-course.html',{'uid':uid,'msg':msg})
    return render(request,'add-course.html',{'uid':uid})

def myprofile(request):
    # global nowtime
    uid=Register.objects.get(email=request.session['email'])
    if request.method=='POST':
        uid.name=request.POST['name']
        uid.mobile=request.POST['mobile']
        uid.address=request.POST['address']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        return render(request,'my-profile.html',{'uid':uid,'msg':'Profile is Updated','nowtime':datetime.datetime.now()})
    return render(request,'my-profile.html',{'uid':uid})
def p404(request):
    return render(request,'404.html')
def p500(request):
    return render(request,'500.html')

def accordion(request):
    return render(request,'accordion.html')
def adddepartment(request):
    uid=Register.objects.get(email=request.session['email'])
    return render(request,'add-department.html',{'uid':uid})
def addlibraryassets(request):
    return render(request,'add-library-assets.html')
def addprofessor(request):
    return render(request,'add-professor.html')
def addstudent(request):
    return render(request,'add-student.html')
def advanceformelement(request):
    return render(request,'advance-form-element.html')
def alerts(request):
    return render(request,'alerts.html')


def allcourses(request):
    return render(request,'all-courses.html')
def allprofessors(request):
    return render(request,'all-professors.html')
def allstudents(request):
    return render(request,'all-students.html')
def analytics(request):
    return render(request,'analytics.html')
def areacharts(request):
    return render(request,'area-charts.html')

def barcharts(request):
    return render(request,'bar-charts.html')
def basicformelement(request):
    return render(request,'basic-form-element.html')
def buttons(request):
    return render(request,'buttons.html')
def c3(request):
    return render(request,'c3.html')
def codeeditor(request):
    return render(request,'code-editor.html')
def courseinfo(request):
    return render(request,'course-info.html')
def coursepayment(request):
    return render(request,'course-payment.html')


def datamaps(request):
    return render(request,'data-maps.html')
def datatable(request):
    return render(request,'data-table.html')
def departments(request):
    return render(request,'departments.html')
def duallistbox(request):
    return render(request,'dual-list-box.html')
def editcourse(request):
    return render(request,'edit-course.html')
def editdepartment(request):
    return render(request,'edit-department.html')
def editlibraryassets(request):
    return render(request,'edit-library-assets.html')
def editprofessor(request):
    return render(request,'edit-professor.html')
def editstudent(request):
    return render(request,'edit-student.html')
def events(request):
    return render(request,'events.html')


def googlemap(request):
    return render(request,'google-map.html')
def imagescropper(request):
    return render(request,'images-cropper.html')
def libraryassets(request):
    return render(request,'library-assets.html')
def linecharts(request):
    return render(request,'line-charts.html')
def lock(request):
    return render(request,'lock.html')
def mailbox(request):
    return render(request,'mailbox.html')
def mailboxcompose(request):
    return render(request,'mailbox-compose.html')
def mailboxview(request):
    return render(request,'mailbox-view.html')
def modals(request):
    return render(request,'modals.html')
def multiupload(request):
    return render(request,'multi-upload.html')
def notifications(request):
    return render(request,'notifications.html')
def passwordmeter(request):
    return render(request,'password-meter.html')   
def pdfviewer(request):
    return render(request,'pdf-viewer.html')
def preloader(request):
    return render(request,'preloader.html')
def professorprofile(request):
    return render(request,'professor-profile.html')
def roundedchart(request):
    return render(request,'rounded-chart.html')
def sparkline(request):
    return render(request,'sparkline.html')
def statictable(request):
    return render(request,'static-table.html')
def studentprofile(request):
    return render(request,'student-profile.html')
def tabs(request):
    return render(request,'tabs.html')
def tinymc(request):
    return render(request,'tinymc.html')
def treeview(request):
    return render(request,'tree-view.html')
def widgets(request):
    return render(request,'widgets.html')
def xeditable(request):
    return render(request,'x-editable.html')
def peity(request):
    return render(request,'peity.html')

