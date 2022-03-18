import email
from django.contrib import admin
from .models import Registraion_model
# Register your models here.
@admin.register(Registraion_model)
class Registraion_admin(admin.ModelAdmin):
    listdisplay=("name","email","phonenumber")