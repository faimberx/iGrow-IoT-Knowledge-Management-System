from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from LOGIN.models import Person, Feed
from .models import *

class PersonForm1(forms.ModelForm):
    class Meta1:  
        model = Person 
        fields = "__all__"  

class UserUpdateForm1(forms.ModelForm):
    Username = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Name = forms.CharField(required=False)
    DateOfBirth = forms.CharField(required=False)
    Age = forms.CharField(required=False)
    District = forms.CharField(required=False)
    State = forms.CharField(required=False)
    Occupation = forms.CharField(required=False)
    About = forms.CharField(required=False)
    Gender = forms.CharField(required=False)
    MaritalStatus = forms.CharField(required=False)

    class Meta1:
        model = Person
        fields = ['Email','Password','Username','Name','DateOfBirth','Age','District','State','Occupation','About','Gender','MaritalStatus']



class UserDeleteForm1(forms.ModelForm):
    class Meta1:
        model = Person
        fields = []


class SharingForm1(forms.ModelForm):
    class Meta1:
        model = Feed
        fields = '__all__'

class CreateInDiscussion1(ModelForm):
    class Meta1:
        model= Group
        fields = '__all__'





