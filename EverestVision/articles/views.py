from django.shortcuts import render, redirect
from .models import Employee ,Customer
from .models import Contact_Form
# Create your views here.
def AdminDashBoard(request):
	employee=Employee.objects.all()
	customer=Customer.objects.all()
	contact=Contact_Form.objects.all()
	return render(request,'AdminPage/AdminDashBoard.html',{'employee':employee,'customer':customer,'contact':contact})

def index(request):
	return render(request,'HomePage/index.html')	

def login(request):
	return render(request,'login.html')

def CustomerRegistrations(request):
	firstname=request.POST["first_name"]
	lastname=request.POST["last_name"]
	address=request.POST["address"]
	contact=request.POST["contact"]
	email=request.POST["email"]
	bookingDate=request.POST["bookingDate"]
	functionName=request.POST["functionName"]
	Customer_form=Customer(first_name=firstname,last_name=lastname,address=address,contact=contact,email=email,bookingDate=bookingDate,functionName=functionName)
	Customer_form.save()
	return render(request,'HomePage/index.html')

def EmployeeRegistrations(request):
	firstname=request.POST["first_name"]
	lastname=request.POST["lastname"]
	address=request.POST["address"]
	contact=request.POST["contact"]
	email=request.POST["email"]
	dob=request.POST["dob"]
	joinningdate=request.POST["joiningdate"]
	specification=request.POST["specification"]
	employee_form=Employee(first_name=firstname,last_name=lastname,address=address,contact=contact,email=email,dob=dob,joiningdate=joinningdate,specification=specification)
	employee_form.save()
	return render(request,'AdminPage/AdminDashBoard.html')


def contact_form_submission(request):
	name=request.POST["name"]
	email=request.POST["email"]
	subject=request.POST["subject"]
	message=request.POST["message"]
	contact_form=Contact_Form(name=name,email=email,subject=subject,message=message)
	contact_form.save()
	return render(request,'HomePage/index.html')


def edit(request , id):
	employees=Employee.objects.get(employee_id=id)
	return render(request,'AdminPage/edit.html',{'employees':employees})

def update(request,id):
	employee=Employee.objects.get(employee_id=id)
	employee_id=id
	firstname=request.POST["first_name"]
	lastname=request.POST["lastname"]
	address=request.POST["address"]
	contact=request.POST["contact"]
	email=request.POST["email"]
	dob=request.POST["dob"]
	joinningdate=request.POST["joiningdate"]
	specification=request.POST["specification"]
	employee_form=Employee(employee_id=employee_id,first_name=firstname,last_name=lastname,address=address,contact=contact,email=email,dob=dob,joiningdate=joinningdate,specification=specification)
	employee_form.save()
	return redirect('/AdminDashBoard')

def delete(request,id):
	Employee.objects.get(employee_id=id)
	user=Employee.objects.get(employee_id=id)
	user.delete()
	return redirect("/AdminDashBoard")

def response(request , id):
	Contact_Form.objects.get(id=id)


def customerlogin(request, id):
	customers=Customer.objects.get(Customer_id=id)
	return render(request,'AdminPage/customerDashBoard.html',{'customers':customers})
