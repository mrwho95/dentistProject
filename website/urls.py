"""dentist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin

#In this directory
from . import views  

urlpatterns = [

	
	
	# user
	path('', views.index, name ="index"),
	path('index.html', views.index, name ="index"),
	path('about-us.html', views.about_us, name ="about_us"),
	path('blog.html', views.blog, name="blog"),
	path('contact.html', views.contact, name="contact"),
	path('department.html', views.department, name="department"),
	path('doctors.html', views.doctors, name="doctors"),
	path('single-blog.html', views.single_blog, name="single_blog"),
	path('element.html', views.element, name="element"),
	path('makeAppointment.html', views.makeAppointment, name="makeAppointment"),
	path('bookAppointment', views.bookAppointment, name="bookAppointment"),

	#admin
	path('adminHome.html', views.adminHome, name= 'adminHome'),
	path('adminCustomerAppointment.html', views.adminCustomerAppointment, name= 'adminCustomerAppointment'),
	path('adminCustomerContact.html', views.adminCustomerContact, name= 'adminCustomerContact'),
	path('adminStaffInfo.html', views.adminStaffInfo, name= 'adminStaffInfo'),
	path('adminAddNewStaff.html', views.adminAddNewStaff, name= 'adminAddNewStaff'),
	path('AddNewStaff', views.AddNewStaff, name='AddNewStaff'),
	path('editStaff/<int:id>', views.editStaff, name='editStaff'),
	path('deleteStaff/<int:id>', views.deleteStaff, name='deleteStaff'),
	path('adminStaffRoster.html', views.adminStaffRoster, name= 'adminStaffRoster'),
	path('adminStaffLeaveApplication.html', views.adminStaffLeaveApplication, name= 'adminStaffLeaveApplication'),

	path('contactRead/<int:id>', views.contactRead, name= 'contactRead'),
	path('contactDelete/<int:id>', views.contactDelete, name= 'contactDelete'),


]
