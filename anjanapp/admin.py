from django.contrib import admin
from anjanapp.models import Employee,Document
# Register your models here.
admin.site.register(Employee) # important we always forget this to create an employee in admin
admin.site.register(Document)