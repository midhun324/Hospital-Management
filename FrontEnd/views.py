from django.shortcuts import render,redirect

from Backend.models import doctordb, deptDB
from FrontEnd.models import signupdb, appointmentdb, contactDb
from django.contrib import messages


# Create your views here.


def homepage(request):
    data=deptDB.objects.all()
    doc=doctordb.objects.all()

    return render(request,"homepage.html",{"data":data,"doc":doc})




def contact(request):
    return render(request,"contact.html")
def service(request):
    return render(request,"service_page.html")




def about(request):
    doc = doctordb.objects.all()
    return render(request,"about_page.html",{"doc":doc})


def department_pg(request):
    return render(request,"department_pg.html")

def login_signup(request):
    return render(request,"register.html")


def save_signup(request):
    if request.method=="POST":
        na=request.POST.get("fullname")
        em=request.POST.get("email")
        pwd=request.POST.get("password")
    obj=signupdb(name=na,email=em,password=pwd)
    obj.save()
    return redirect(login_signup)

def UserLogin(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        if signupdb.objects.filter(name=uname,password=pwd).exists():
            request.session["username"]=uname
            request.session["password"]=pwd
            messages.success(request, "Sucessfully Log In")
            return redirect(homepage)
        else:
            messages.error(request, "invalid Username or Password")
            return redirect(login_signup)
        messages.error("invalid Username or Password")
    return redirect(login_signup)

def user_Logout(request):
    del request.session["username"]
    del request.session["password"]
    return redirect(login_signup)



def make_appointment(request):
    if request.method=="POST":
        dept=request.POST.get("dept")
        doc=request.POST.get("doc")
        dt=request.POST.get("date")
        tm=request.POST.get("time")
        na=request.POST.get("name")
        date_of_birth=request.POST.get("dob")
        em=request.POST.get("email")
        gen=request.POST.get("Gender")
        num=request.POST.get("phone")
        mess=request.POST.get("message")
        obj=appointmentdb(department=dept,doctor=doc,date=dt,time=tm,name=na,dob=date_of_birth,email=em,gender=gen,number=num,message=mess)
        obj.save()
        messages.success(request, "Appointment Booked")
        return redirect(homepage)
def department_pg(request):
    dept=deptDB.objects.all()
    return render(request,"department_pg.html",{"dept":dept})



def single_dept(request,dept_id):
    data=deptDB.objects.get(id=dept_id)
    return render(request,"single_department.html",{"data":data})


def appointment_page(request):
    return render(request,"appointment_page.html")



def confirmation_pg(request):
    return render(request,"confirmation_page.html")


def make_appointment_2(request):
    if request.method=="POST":
        dept=request.POST.get("dept")
        doc=request.POST.get("doc")
        dt=request.POST.get("date")
        tm=request.POST.get("time")
        na=request.POST.get("name")
        date_of_birth=request.POST.get("dob")
        em=request.POST.get("email")
        gen=request.POST.get("Gender")
        num=request.POST.get("phone")
        mess=request.POST.get("message")
        obj=appointmentdb(department=dept,doctor=doc,date=dt,time=tm,name=na,dob=date_of_birth,email=em,gender=gen,number=num,message=mess)
        obj.save()
        messages.success(request, "Appointment Booked")
        return redirect(confirmation_pg)



def doctor_page(request):
    doc=doctordb.objects.all()
    return render(request,"doctor_page.html",{"doc":doc})


def single_doctor(request,doc_id):
    doc=doctordb.objects.get(id=doc_id)
    return render(request,"single_doctor.html",{"doc":doc})


def blog_page(request):
    return render(request,"blog_page.html")
def single_blog(request):
    return render(request,"single_blog.html")


def save_contact(request):
    if request.method=="POST":
        na=request.POST.get("name")
        em=request.POST.get("email")
        qu=request.POST.get("subject")
        num=request.POST.get("phone")
        mess=request.POST.get("message")
        obj=contactDb(name=na,email=em,query=qu,number=num,message=mess)
        obj.save()
        messages.success(request,"Message Sent Successfully")
        return redirect(contact)


