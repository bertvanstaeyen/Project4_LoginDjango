from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from social_core.backends import username

from .models import Profile


class SetPasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


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

    serialNumber = forms.CharField(max_length=50,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Serial Number',
                                                              'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                              'id': 'serialNumber',
                                                              }))

    def clean_email(self):
         email = self.cleaned_data['email']
         if User.objects.filter(email=email).exists():
             raise ValidationError("Email already exists")
         return email

    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'serialNumber']


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
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput( attrs={"id":"rememberme", "name":"rememberme", "class": "w-4 h-4 text-primary-normal bg-gray-100 border-gray-300 rounded focus:ring-primary-normal focus:ring-2 mr-2"}))


    def clean_email(self):
         email = self.cleaned_data['email']
         if User.objects.filter(email=email).exists():
             raise ValidationError("Email already exists")
         return email

    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return user
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5'}))
    

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none'}))

    serialNumber = forms.CharField(max_length=50,
                                   required=True,
                                   widget=forms.TextInput(attrs={'placeholder': 'Serial Number',
                                                                 'class': 'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-normal focus:border-primary-normal block w-full p-2.5',
                                                                 'id': 'serialNumber',
                                                                 }))
    class Meta:
        model = Profile
        # fields = ['avatar', 'serialNumber']
        fields = ['serialNumber']
