from django.shortcuts import redirect, render
from django.http import HttpResponseBadRequest,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import razorpay
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
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if uid.password == request.POST['opassword']:
            if request.POST['npassword'] == request.POST['ncpassword']:
                uid.password = request.POST['npassword']
                uid.save()
                return render(request,'index.html',{'uid':uid,'msg':'Password Updated'})
            return render(request,'change-password.html',{'uid':uid,'msg':'Both new are not same'})
        return render(request,'change-password.html',{'uid':uid,'msg':'Old Password is wrong'})
    return render(request,'change-password.html',{'uid':uid,'msg':'Please feel the currect data'})
    

def forgot(request):
    return render(request,'forgot.html')

def about(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'about.html',{'uid':uid})
    except:
        return render(request,'about.html')

def all_courses(request):
    courses = All_Course.objects.filter(covarify=False,coreject=False)[::-1]
    if request.POST:
            courses = All_Course.objects.filter(coname__contains =request.POST['scourse'])
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'all-courses.html',{'courses':courses,'uid':uid})
    except:
        return render(request,'all-courses.html',{'courses':courses})


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
        index = Add_Index.objects.filter(course=course)[::-1]
        print(index)
        course.views.add(uid)
        return render(request,'course-details.html',{'uid':uid,'course':course,'index':index})
    except:
        course = All_Course.objects.get(id=pk)
        index = Add_Index.objects.filter(course=course)
        return render(request,'course-details.html',{'course':course,'index':index})

def dashboard(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        book = Booking.objects.filter(student=uid,pay_verify=True)
        return render(request,'dashboard.html',{'uid':uid,'book':book})
    except:
        return redirect('login')


def db_courses(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        book = Booking.objects.filter(student=uid,pay_verify=True)
        return render(request,'db-courses.html',{'uid':uid,'book':book})
    except:
        return render(request,'login.html')


def wish_list(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        cart = Cart.objects.get(student=uid)
        cart_count = cart.cart.all().count()
        return render(request,'db-exams.html',{'uid':uid,'cart':cart,'cc':cart_count})
    except:     
        return render(request,'db-exams.html')

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

# def db_time_line(request):
#     uid = User.objects.get(email=request.session['email'])
#     return render(request,'db-time-line.html',{'uid':uid})

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

    
def payment(request,pk):
    try:
        uid = User.objects.get(email=request.session['email'])  
    except:
        return render(request,'login.html')
    co =All_Course.objects.get(id=pk)
    # if request.method == 'POST':
    book = Booking.objects.create(
        student = uid,
        course=co,
    )        
    currency = 'INR'
    amount = int(co.coprice)*100  # Rs. 200

    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                    currency=currency,
                                                    payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = f'paymenthandler/{book.id}'

    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['uid'] = uid
    context['co'] = co
    context['book'] = book
    return render(request,'payment.html',context=context)

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request,pk):
    uid = User.objects.get(email=request.session['email'])
    book = Booking.objects.get(id=pk)
    # only accept POST request.
    if request.method == "POST":
        try:     
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            # if result is None:
            amount = int(book.course.coprice)*100  # Rs. 200
            try:

                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)
                book.pay_verify = True
                book.pay_id = payment_id
                book.save()
                # render success page on successful caputre of payment
                return render(request, 'success.html',{'uid':uid,'book':book})
            except:

                # if there is an error while capturing payment.
                return render(request, 'fail.html',{'uid':uid})
            # else:

            #     # if signature verification fails.
            #     return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()


def cart(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        course = All_Course.objects.get(id=request.GET['id'])
        try:
            cart = Cart.objects.get(student=uid)
        except:
            cart = Cart.objects.create(student=uid)
        print(cart)
        cart.cart.add(course)
        return JsonResponse({'msg':'Added To Cart'})
    except:
        return JsonResponse({'msg':'Please Login and Try Again'})
    
def review(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        if request.method == 'POST':
            course = All_Course.objects.get()        
            view=Review.objects.create(
                name = request.POST['name'],
                email = request.POST['email'],
                msg = request.POST['msg'],
            )
            return render(request,'review.html',{'uid':uid,'course':course,'view':view,'msg':'Your Review is Added'})
        return render(request,'review.html',{'uid':uid})
    except:
        return redirect('login')
    
def view_course(request,pk):
    uid = User.objects.get(email=request.session['email'])
    course = All_Course.objects.get(id=pk)
    index = Add_Index.objects.filter(course=course)[::-1]
    return render(request,'view-course.html',{'uid':uid,'course':course,'index':index})




def game1(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'game1.html',{'uid':uid})
def game3(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'game3.html',{'uid':uid})
def game2(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'game2.html',{'uid':uid})
def game4(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'game4.html',{'uid':uid})
def game5(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'game5.html',{'uid':uid})