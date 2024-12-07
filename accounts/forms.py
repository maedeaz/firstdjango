from django import forms
from django.contrib.auth.models import User
from .models import *

error = {
    'min_length' : 'حداکثر می بایست 5 کاراکتر باشد' ,
    'required' : 'این فیلد الزامی است',
}




class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length=50 ,widget=forms.TextInput(attrs={'placeholder' : 'نام کاربری ...'}) , error_messages=error)
    email = forms.EmailField(error_messages=error)
    first_name = forms.CharField(max_length=10 , min_length=5 , widget=forms.TextInput(attrs = {'placeholder' : 'نام خود را وارد نمایید'}) , error_messages=error)
    last_name = forms.CharField(max_length=100 , error_messages=error)
    password_1 = forms.CharField(max_length=50 , widget=forms.PasswordInput(attrs={'placeholder' : 'password...'}) , error_messages=error)
    password_2 = forms.CharField(max_length=50 , widget=forms.PasswordInput(attrs={'placeholder' : 'password...'}) , error_messages=error)

    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username = user).exists():
            raise  forms.ValidationError('نام کاربری تکراری است')
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists() :
            raise forms.ValidationError('پست الکترونیکی تکراری است')
        return email

    def clean_password_2(self):
        pass1 = self.cleaned_data['password_1']
        pass2 = self.cleaned_data['password_2']
        if pass1 != pass2 :
            raise forms.ValidationError('پسورد مطابقت ندارد')
        elif len(pass2) < 8 :
            raise forms.ValidationError('پسورد می بایست حداقل 8 کاراکتر باشد')
        elif not any (x.isupper() for x in pass2):
            raise forms.ValidationError('پسورد می بایست دارای یک حرف بزرگ باشد')
        return pass2


class UserLoginForm(forms.Form) :
    user = forms.CharField()
    password = forms.CharField()



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email' , 'first_name' , 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone' , 'address']