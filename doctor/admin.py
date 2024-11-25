from django.contrib import admin
from .models import Doctor
# Register your models here.

class ToDoctor(admin.ModelAdmin):
    list_display = ['first_name','last_name','specialty']
    
admin.site.register(Doctor,ToDoctor)

