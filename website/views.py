from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
# def home(request):
# 	return render(request, 'index.html', {})

def index(request):
	return render(request, 'index.html', {})

def about_us(request):
	return render(request, 'about-us.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST.get('name')
		message_email = request.POST.get('email')
		message_content = request.POST.get('content')
		message_subject = request.POST.get('subject')

		#send an email
		# send_mail(
		# 	message_subject, #subject
		# 	message_content, #content
		# 	message_email, #from email
		# 	['dnkh903@gmail.com'], #to email 
		# 	)

		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})

def department(request):
	return render(request, 'department.html', {})

def doctors(request):
	return render(request, 'doctors.html', {})

def single_blog(request):
	return render(request, 'single-blog.html', {})

def element(request):
	return render(request, 'element.html', {})





