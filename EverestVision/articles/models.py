from django.db import models

# Create your models here.
class Employee(models.Model):
	employee_id=models.AutoField(auto_created=True,primary_key=True)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	contact=models.CharField(max_length=20)
	email=models.EmailField(max_length=30,unique=True)
	joiningdate=models.DateField(auto_now=False, auto_now_add=True,)
	dob=models.DateField(auto_now=False, auto_now_add=False,)
	specification=models.CharField(max_length=50)
	class meta:
		db_table="employee"



class Customer(models.Model):
	Customer_id=models.AutoField(auto_created=True,primary_key=True)
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=30)
	address=models.CharField(max_length=50)
	contact=models.CharField(max_length=20)
	email=models.EmailField(max_length=30,unique=True)
	bookingDate=models.DateField(auto_now=False, auto_now_add=True,)
	functionName=models.CharField(max_length=50)
	class meta:
		db_table="customer"


class Contact_Form(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=30,unique=True)
	subject=models.CharField(max_length=50)
	message=models.TextField(max_length=500)
	class meta:
		db_table="message"