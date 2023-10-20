from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from Backend.models import doctordb, deptDB
from FrontEnd.models import appointmentdb


# Create your views here.


def doctor(request):
    doc=deptDB.objects.all()
    return render(request, "doctors_reg.html",{"doc":doc})


def index(request):
    return render(request, "index.html")


def doctor_reg(request):
    if request.method == "POST":
        na = request.POST.get("fname")
        uname = request.POST.get("uname")
        imag = request.FILES["img"]
        ads = request.POST.get("adrs")
        desc = request.POST.get("description")
        pwd = request.POST.get("pwd")
        dp = request.POST.get("dp")
        cnt = request.POST.get("cnt")
        em = request.POST.get("email")
        obj = doctordb(name=na, username=uname, image=imag, address=ads, password=pwd,description=desc,email=em, department=dp, contact=cnt)
        obj.save()
    return redirect(doctor)


def dotors_record(request):
    data = doctordb.objects.all()

    return render(request, "doctor_details.html", {"data": data})


def edit_doctor(request, dataid):
    data = doctordb.objects.get(id=dataid)
    return render(request, "edit_doctor.html", {"data": data})


def delete_doc(request, dataid):
    data = doctordb.objects.get(id=dataid)
    data.delete()
    return redirect(dotors_record)


def update_doc(request, dataid):
    if request.method == "POST":
        na = request.POST.get("fname")
        adrs = request.POST.get("adrs")
        desc = request.POST.get("description")
        dp = request.POST.get("dp")
        cnt = request.POST.get("cnt")
        em = request.POST.get("email")

    try:
        img = request.FILES["image"]
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = doctordb.objects.get(id=dataid).image
    doctordb.objects.filter(id=dataid).update(name=na, address=adrs, department=dp,description=desc,email=em, contact=cnt, image=file)
    return redirect(dotors_record)


def view_doctor(request):
    return render(request, "view_doctor.html")


def Login_page(request):
    return render(request,"login_page.html")

def admin_login(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        pwd=request.POST.get("password")
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pwd
                return redirect(index)
            else:
                return redirect(Login_page)
        else:
            return redirect(Login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Login_page)


def department(request):
    return render(request,"department_page.html")


def save_dept(request):
    if request.method=="POST":
        dept=request.POST.get("dept")
        desc=request.POST.get("desc")
        img=request.FILES["img"]
        obj=deptDB(department=dept,description=desc,image=img)
        obj.save()
        return redirect(department)


def dept_details(request):
    dept=deptDB.objects.all()
    return render(request,"dept_details.html",{"dept":dept})

def edit_dept(request,dept_id):
    dept = deptDB.objects.get(id=dept_id)
    return render(request,"edit_dept.html",{"dept":dept})


def update_dept(request, dept_id):
    if request.method == "POST":
        dept = request.POST.get("dept")
        desc = request.POST.get("desc")


    try:
        img = request.FILES["img"]
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = deptDB.objects.get(id=dept_id).image
    deptDB.objects.filter(id=dept_id).update(department=dept,description=desc, image=file)
    return redirect(dept_details)


def delete_dept(request,dept_id):
    data=deptDB.objects.get(id=dept_id)
    data.delete()
    return redirect(dept_details)


def appointment_details(request):
    data=appointmentdb.objects.all()
    return render(request,"appointment_details.html",{"data":data})

def delete_ap(request,ap_id):
    data = appointmentdb.objects.get(id=ap_id)
    data.delete()
    return redirect(appointment_page)