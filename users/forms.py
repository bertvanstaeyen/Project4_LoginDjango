from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from social_core.backends import username

from .models import Profile, SerialNumber


# This class is used to set passwords for users.
class SetPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


# This form is used to register a new account on the application.
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                                  'id': 'password',
                                                                  }))

    # This definition is used to check if the email already exists.
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    # This definition is used to check if the username already exists.
    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


# This class is used to add serial numbers to a profile.
class SerialNumberForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                         'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                         'id': 'serialNumber',
                                                         }))

    serialNumber = forms.CharField(max_length=50,
                                   required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Serial Number',
                                                                 'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                                 'id': 'serialNumber',
                                                                 }))

    class Meta:
        model = SerialNumber
        fields = ["serialNumber", "name"]


# This class is used to log in to the application
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'shadow-sm border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'shadow-sm border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                                 #  'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={"id": "rememberme", "name": "rememberme",
               "class": "w-4 h-4 text-primary-normal bg-gray-100 border-gray-300 rounded focus:ring-primary-normal focus:ring-2 mr-2"}))

    # This definition is used again to check if the email exists.
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    # This definition is used again to check if the username exists.
    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


# This class is used to update a user, for example change the username..
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={
                                   'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5'}))

    class Meta:
        model = User
        fields = ['username', 'email']
