from django.contrib import admin
from .models import Doctor, Staff
from .models import Contact

# Regiser models to admin site
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Contact)
admin.site.register(Staff)
