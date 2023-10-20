from django.db import models

# Create your models here.
class deptDB(models.Model):
    department=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to="department",null=True,blank=True)




class doctordb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to="doctor_profile",null=True,blank=True)
    email=models.EmailField(null=True,blank=True,max_length=50)
    address=models.CharField(max_length=100,null=True,blank=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    department=models.CharField(max_length=100,null=True,blank=True)
    contact=models.CharField(max_length=100,null=True,blank=True)




