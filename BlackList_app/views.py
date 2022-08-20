from django.shortcuts import render

from audioop import add
import email
from gettext import translation
from multiprocessing.dummy import connection
from site import addusersitepackages
from tkinter.tix import Select
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . import addUsersToDatabase
from . import addComplainsToDatabase
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db import connections
from .models import Users,Complain,UserPic

def homepage(request):
    return render(request,'homepage.html')

def login(request):
    if request.method=='POST':
        username=request.POST['userName']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('BlackList_app:menu_student')
        else:
            messages.info(request,'Credentials given are wrong')
            return redirect('BlackList_app:login')
    else:
        return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        fullname=request.POST['userName']
        userName=request.POST['studentId']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        
        if password==confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('BlackList_app:login')
            elif User.objects.filter(username=userName).exists():
                messages.info(request,'ID already exists')
                return redirect('BlackList_app:login')
            else:
                #saving user in django admin panel and django user saver
                user = User.objects.create_user(username=userName, email=email, password=password)
                user.save();
                
                #sending data to the user database to register the user through useradd class
                userRegistration=addUsersToDatabase.UserAdd(userName,fullname,email)
                userRegistration.addUser()
                
                return redirect('BlackList_app:login')
        else:
            messages.info(request, 'Two passwords did not match')
            return redirect('BlackList_app:login')
    else:
         return render(request, 'login.html')

@login_required
def menu_student(request):
    return render(request,"menu_student.html")

def menu_institution(request):
    return render(request,"menu_institution.html")

@login_required
def complaint(request):
    if request.method=="POST":
        studentId=request.POST['studentId']
        #add file database variable here after handling media query
        description=request.POST['description']
        links=request.POST['links']
        
        anonimity='True' #change this after html gets corrected as it shows unwanted stuff while selecting the option
        
        addingComplaint=addComplainsToDatabase.RegisterComplains(studentId,description,links,anonimity)
        addingComplaint.registerComplains()
        
    #Complete this
        
    return render(request,"complaint.html")

@login_required
def notifications(request):
    return render(request,"notifications.html")

@login_required
def profile(request):
    current_user=request.user
    studentid = str(current_user.username)
    
    person=Users.objects.raw("SELECT * FROM BlackList_app_users WHERE userid='"+studentid+"'")         
    foruserPicture=UserPic.objects.raw("SELECT * FROM BlackList_app_userpic WHERE userid_id='"+studentid+"'")
    userpicUrl=''
    for userpic in foruserPicture:
        userpicUrl='images/'+str(userpic.picture)
    userid=''
    name=''
    email=''
    for person in person:
        userid=person.userid
        name=person.name
        email=person.email
    print(studentid)
    complainFinder=Complain.objects.raw("SELECT * FROM BlackList_app_complain WHERE bully_id='"+studentid+"'")
    complaints=[]
    for complains in complainFinder:
        description=complains.abuseDescription
        complaints.append(description)    
    print(complaints)
    context={'studentid':userid,'name':name,'email':email,'complain':complaints,'userpic':userpicUrl}
    print(context)
    return render(request,"profile.html",context)

@login_required
def messege(request):
    return render(request,"messege.html")

