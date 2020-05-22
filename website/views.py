from django.shortcuts import render
from django.core.mail import send_mail
from .models import Doctor  #import {class name from model file}
from .models import Contact

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





