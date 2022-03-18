from registration.models import Registraion_model
from django import forms
# 
class RegistraionForm(forms.ModelForm):
    class Meta:
        model=Registraion_model
        exclude=()

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phonenumber":forms.TextInput(attrs={"class":"form-control"}),
        }
