from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Staff, Appointment

class StaffForm(forms.ModelForm):
	class Meta:
		model = Staff
		field = [
			'staffID',
			'name',
			'email',
			'age',
			'phone',
			'address',
			'position',
			'department'
		]
		exclude = ()

class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		field = ['name', 'NRIC', 'email', 'phone', 'date', 'time']
		exclude = ()

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

