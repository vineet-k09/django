from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username=forms.CharField(label="Username", max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username','required':True}))
    email=forms.EmailField(label="E-mail", max_length=40 , widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email','required':True}))
    password=forms.CharField(label="Password", max_length=50 ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password','required':True}))
    confirm_password=forms.CharField(label="Confirm password", max_length=50 ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Confirm password','required':True}))

    def clean(self):
        cleaned_data=super().clean()
        if self.errors:
            return self.cleaned_data
        valid_password=cleaned_data['password']
        valid_confirm_password=cleaned_data['confirm_password']

        if valid_password!= valid_confirm_password:
            raise forms.ValidationError("Password Mismatched")
    
    class Meta:
        model=User
        fields=['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class ContactForm(forms.Form):
    name=forms.CharField(label="Name", max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username','required':True}))
    email=forms.CharField(label="E-mail", max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'E-mail','required':True}))
    message=forms.CharField(label="Message",max_length=500, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your messsage','required':True}))

    def clean(self):
        cleaned_data=super().clean()
        if self.errors:
            return self.cleaned_data
        valid_name=cleaned_data['name']

        if len(valid_name)<3:
            raise forms.ValidationError("Minimum of 3 Characters")

class LoginForm(forms.Form):
    username=forms.CharField(label="Username", max_length=40, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username','required':True}))
    password=forms.CharField(label="Password", max_length=50 ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Password','required':True}))

    def clean(self):
        if self.errors:
            return self.cleaned_data