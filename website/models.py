from django.db import models

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 100)
	age = models.IntegerField()
	department = models.CharField(max_length = 100)

	def __str__(self):
		return self.name + ' ' + self.email