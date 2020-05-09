from django.shortcuts import render

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
	return render(request, 'contact.html', {})

def department(request):
	return render(request, 'department.html', {})

def doctors(request):
	return render(request, 'doctors.html', {})

def single_blog(request):
	return render(request, 'single-blog.html', {})

def element(request):
	return render(request, 'element.html', {})





