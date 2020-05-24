from django import forms

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