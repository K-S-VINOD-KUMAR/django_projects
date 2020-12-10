from django.forms import ModelForm

from Tollywood.models import *

class UserForm(ModelForm):
    class Meta:
        model=Userregister
        fields="__all__" #['name','name2]