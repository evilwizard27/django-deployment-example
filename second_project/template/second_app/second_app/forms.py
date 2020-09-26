from django import forms
from django.contrib.auth.models import User
from second_app.models import userprofile

class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class profileform(forms.ModelForm):
    class Meta():
        model = userprofile
        fields = ('f_name','profile_pic')
