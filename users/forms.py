from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
    #  widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'})
    password1 = forms.CharField(widget=forms.PasswordInput( attrs={'class':'form-control','placeholder':'Password'}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput( attrs={'class':'form-control','placeholder':'Confirm Password'}),label='Confirm Password')
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        labels = {
            'email':'Email Address',
            'password1':'Password',
            'password2':'Confirm Password',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
