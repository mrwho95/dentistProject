from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Doctor, Contact, Staff #import {class name from model file}
from .forms import StaffForm
import sweetify
import uuid


# Create your views here.
# def home(request):
# 	return render(request, 'index.html', {})

def index(request):
	return render(request, 'user/index.html', {})

def about_us(request):
	return render(request, 'user/about-us.html', {})

def blog(request):
	return render(request, 'user/blog.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST.get('name')
		message_email = request.POST.get('email')
		message_content = request.POST.get('message')
		message_subject = request.POST.get('subject')

		#send an email
		# send_mail(
		# 	message_subject, #subject
		# 	message_content, #content
		# 	message_email, #from email
		# 	['dnkh903@gmail.com'], #to email 
		# 	)

		storeContact = Contact(name= message_name, email= message_email, content= message_content, subject = message_subject)
		storeContact.save()

		return render(request, 'user/contact.html', {'message_name': message_name})
	else:
		return render(request, 'user/contact.html', {})

def department(request):
	return render(request, 'user/department.html', {})

def doctors(request):
	allDoctors = Doctor.objects.all
	return render(request, 'user/doctors.html', {'doctor': allDoctors})

def single_blog(request):
	return render(request, 'user/single-blog.html', {})

def element(request):
	return render(request, 'user/element.html', {})


#admin
def adminHome(request):
	return render(request, 'admin/home.html', {})

def adminCustomerAppointment(request):
	return render(request, 'admin/customerAppointment.html', {})

def adminCustomerContact(request):
	customerContactDataset = Contact.objects.all
	return render(request, 'admin/customerContact.html', {'contactDataset': customerContactDataset})

def contactRead(request, id):
	customerContact = Contact.objects.get(id = id)
	customerContact.read = True
	customerContact.save()
	# sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
	messages.success(request, 'The contact message is done to read!')
	return redirect('/adminCustomerContact.html')

def contactDelete(request, id):
	customerContact = Contact.objects.get(id = id)
	customerContact.delete()
	# sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
	messages.success(request, 'Successfully to delete contact message!')
	return redirect('/adminCustomerContact.html')

def adminStaffInfo(request):
	staffData = Staff.objects.all
	return render(request, 'admin/staff.html', {'staffDataset': staffData})

def adminAddNewStaff(request):
	ID = uuid.uuid4()
	return render(request, 'admin/addNewStaff.html', {'staffID': ID})

def AddNewStaff(request):
	if request.method == 'POST':
		form = StaffForm(request.POST)
		if form.is_valid(): 
			form.save()
			messages.success(request, 'Successfully to add new staff!')
			return HttpResponseRedirect('/adminStaffInfo.html')
		else:
			pass 
			#no operation
	else:
		form = StaffForm()
		return render(request, 'admin/addNewStaff.html', {'form': form})

	

def adminStaffRoster(request):
	return render(request, 'admin/staffRoster.html', {})

def adminStaffLeaveApplication(request):
	return render(request, 'admin/staffOnLeave.html', {})



