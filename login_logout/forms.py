from django import forms
from django.contrib.auth.models import User
import datetime
from django.forms.extras.widgets import SelectDateWidget
from .models import UserInfo

choice = (
	('M', 'M'),
	('F', 'F'),
	)
class DateInput(forms.DateInput):
    input_type = 'date'
    
class UserRegistrationForm(forms.ModelForm):
	Gender = forms.ChoiceField(choices=choice, required=True)
	#BirthDate = forms.DateField(widget=SelectDateWidget)
	class Meta:
		model = UserInfo
		fields = ['FullName' , 'ProfilePic', 'BirthDate' ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']