from django.db import models

# Create your models here.
class Doctor(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 100)
	age = models.IntegerField()
	department = models.CharField(max_length = 100)

	def __str__(self):
		return self.name + ' ' + self.email

class Contact(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 100)
	content = models.CharField(max_length = 100)
	subject = models.CharField(max_length =100)
	read = models.BooleanField(default=False)

	def __str__(self):
		return "A new message: "+ self.subject + ' which sent by ' + self.name

class Staff(models.Model):
	staffID = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 100)
	age = models.IntegerField(null = True)
	phone = models.CharField(max_length = 50, null = True)
	address = models.CharField(max_length = 200)
	position = models.CharField(max_length = 100)
	department = models.CharField(max_length = 100)

	def __str__(self):
		return "Staff "+ self.name

class Appointment(models.Model):
	name = models.CharField(max_length=100)
	NRIC = models.CharField(max_length=20)
	email = models.EmailField(max_length = 100)
	phone = models.CharField(max_length = 50 , null = True)
	date= models.DateField(null = False)
	time = models.CharField(null = False, max_length=50)

	def __str__(self):
		return self.name+ " got appointment on " + str(self.date)

# class Admin(models.Model):
# 	username = models.CharField(max_length=100)
# 	fullname = models.CharField(max_length = 100)
# 	email = models.CharField(max_length = 50)
# 	password = models.CharField(max_length = 50, null=True)
# 	admin = models.BooleanField(default = True)