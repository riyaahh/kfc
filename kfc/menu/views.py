from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import userdetails
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,"menu/index.html",context={})



def signin(request):
    
    if request.method == "POST":
        print('here')
        email=request.POST.get('email')
        pasword=request.POST.get('password')
        user=authenticate(request, username=email,password=pasword)
        print('here2')
        if user is not None:
            print('here3')
            if user.is_superuser:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("Admin User")
            elif user.is_staff:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("page1")
            else:
                login(request,user)
                request.session['admin_id']=user.id
                return redirect("profileform",user.id)
        else:
            msg='invalid details'
            return render(request,'menu/index.html',{'msg':msg})
    else:
            return render(request,'menu/index.html')
 

def registration(request):
    errors={}
    if request.method=='POST':

        firstname=request.POST.get('firstName')
        lastname=request.POST.get('secondName')
        emailid=request.POST.get('email')
        password=request.POST.get('password')
        phoneno=request.POST.get('phoneNo')
        gender=request.POST.get('Gender')


        new_user=User.objects.create_user(first_name=firstname,last_name=lastname,password=password,username=emailid)
        new_user.save()

        ud=userdetails.objects.create(user=new_user,gender=gender,emailid=emailid,phoneno=phoneno)
        ud.save()
        return redirect('index')
    else:
        return render(request,"menu/registration.html",context={})
    
def page1(request):
    return render(request,"menu/page1.html",context={})

def page2(request):
    return render(request,"menu/page2.html",context={})

def profileform(request,id):
    return render(request,"menu/profileform.html",context={'id':id})

def updateform(request,id):
    user=userdetails.objects.get(user=id)
    
    if request.method=="POST":
        gender=user.gender
        print('here')
        user.phoneno=request.POST.get('phone')
        user.emailid=request.POST.get('email')
        user.gender=gender
        user.save()
        return redirect("profileform",id)
    return render(request,'menu/updateform.html',{'user':user,'id':id})
    

def delete(request,id):
    task=userdetails.objects.get(user=id)
    task.delete()
    return redirect('index')


def table(request,id):
    return render(request,"menu/table.html",context={'id':id})