from django import forms

from .models import Staff

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