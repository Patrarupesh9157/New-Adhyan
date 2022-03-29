from django.shortcuts import redirect, render
from .models import *
from Myapp.models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange

# Create your views here.
def index(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        courses = All_Course.objects.filter(covarify=False,coreject=False)[::-1]
        return render(request,'index.html',{'uid':uid,'courses':courses})
    except:
        courses = All_Course.objects.filter(covarify=False,coreject=False)[::-1]
        return render(request,'index.html',{'courses':courses})

def register(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            return render(request,'register.html',{'msg':'Your Email is already registered'})
        except:
            if request.POST['password']==request.POST['cpassword']:
                global temp
                temp={
                    'name' : request.POST['name'],
                    'gender' : request.POST['gender'],
                    'dob' : request.POST['dob'],
                    'mobile' : request.POST['mobile'],
                    'email' : request.POST['email'],
                    'address' : request.POST['address'],
                    'password' : request.POST['password']
                }
                otp = randrange(1000,9999)
                subject = 'welcome to Lab App'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'otp.html',{'otp':otp})
            return render(request,'login.html',{'msg':'Account is Created'})
    return render(request,'register.html')

def login(request):
    try:
        User.objects.get(email=request.session['email'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = User.objects.get(email=request.POST['email'])
                if uid.password == request.POST['password']:
                    request.session['email'] = uid.email
                    return redirect('index')
                return render(request,'login.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'register.html',{'msg':'Email is not registered'})
        return render(request,'login.html')

def otp(request):
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            
            User.objects.create(
                name = temp['name'],
                gender = temp['gender'],
                dob = temp['dob'],
                email = temp['email'],
                mobile = temp['mobile'],
                address = temp['address'],
                password = temp['password']
            )
            msg = "Account is Created"
            return render(request,'login.html',{'msg':msg})
        return render(request,'otp.html',{'otp':request.POST['otp'],'msg':'incorrect OTP'})
    return redirect('register')

def logout(request):
    del request.session['email']
    return redirect('index')

def change_password(request):
    del request.session['email']
    return redirect('index')

def forgot(request):
    return render(request,'forgot.html')

def about(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'about.html',{'uid':uid})
    except:
        return render(request,'about.html')

def all_courses(request):
    uid = User.objects.get(email=request.session['email'])
    courses = All_Course.objects.filter(covarify=False,coreject=False)[::-1]
    if request.POST:
        courses = All_Course.objects.filter(coname__contains =request.POST['scourse'])
    return render(request,'all-courses.html',{'courses':courses,'uid':uid})

def contact_us(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        if request.method == 'POST':
            Enquiry.objects.create(
                name=request.POST['name'],
                mobile=request.POST['mobile'],
                email=request.POST['email'],
                city=request.POST['city'],
                des=request.POST['des']
            )
            msg='Complant is Added'
            return render(request,'contact-us.html',{'msg':msg})
        return render(request,'contact-us.html',{'uid':uid})
    except:
        if request.method == 'POST':
            Enquiry.objects.create(
                name=request.POST['name'],
                mobile=request.POST['mobile'],
                email=request.POST['email'],
                city=request.POST['city'],
                des=request.POST['des']
            )
            msg='Complant is Added'
            return render(request,'contact-us.html',{'msg':msg})
        return render(request,'contact-us.html')

def admission(request):

    return render(request,'admission.html')

def awards(request):
    return render(request,'awards.html')

def course_details(request,pk):
    try:
        uid = User.objects.get(email=request.session['email'])
        course = All_Course.objects.get(id=pk)
        course.views.add(uid)
        return render(request,'course-details.html',{'uid':uid,'course':course})
    except:
        return render(request,'course-details.html')

def dashboard(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'dashboard.html',{'uid':uid})
    except:
        return redirect('login')


def db_courses(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'db-courses.html',{'uid':uid})
    except:
        return render(request,'db-courses.html')


def db_exams(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'db-exams.html',{'uid':uid})

def db_profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.gender = request.POST['gender']
        uid.mobile = request.POST['mobile']
        uid.email = request.POST['email']
        uid.address = request.POST['address']
        uid.password = request.POST['password']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        return render(request,'db-profile.html',{'uid':uid,'msg':'Profile Updated'})
    return render(request,'db-profile.html',{'uid':uid})

def db_time_line(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'db-time-line.html',{'uid':uid})

def departments(request):
    return render(request,'departments.html')

def event_details(request):
    return render(request,'event-details.html')

def event_register(request):
    return render(request,'event-register.html')

def events(request):
    return render(request,'events.html')

def facilities_details(request):
    return render(request,'facilities-details.html')

def facilities(request):
    return render(request,'facilities.html')

def gallery_photo(request):
    return render(request,'gallery-photo.html')

def research(request):
    return render(request,'research.html')

def seminar(request):
    return render(request,'seminar.html')
