from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, SerialNumberForm
from .forms import SetPasswordForm

from .models import Profile

@login_required
def homeDay(request):
    user = request.user
    return render(request, 'users/home-day.html', {'username': user.username})

@login_required
def homeWeek(request):
    user = request.user
    return render(request, 'users/home-week.html', {'username': user.username})

@login_required
def homeMonth(request):
    user = request.user
    return render(request, 'users/home-month.html', {'username': user.username})

@login_required
def serialNumber(request):
    
    # user = request.user
    # profile = user.profile
    # numbers = profile.serialnumber_set.all()
    # for number in numbers:
    #     print(number.id)

    if request.method == 'POST':
        form = SerialNumberForm(data=request.POST)
        if form.is_valid():
            print('valid')
            new_serialnumber = form.save(commit=False)
            new_serialnumber.owner_id = request.user.id
            new_serialnumber.save()
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    return render(request, 'users/crud-serial-number.html', {'form': SerialNumberForm()})

def help(request):
    return render(request, 'users/help.html')

class RegisterView(View):
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        serialNumberForm = SerialNumberForm(initial=self.initial)
        registerForm = RegisterForm(initial=self.initial)
        return render(request, self.template_name, {'SerialForm': serialNumberForm, "RegisterForm": registerForm})

    def post(self, request, *args, **kwargs):

        serialNumberForm = SerialNumberForm(request.POST)
        registerForm = RegisterForm(request.POST)

        if serialNumberForm.is_valid() and registerForm.is_valid():
            registerForm.save()
            serialNumberForm.save()

            username = registerForm.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'SerialForm': serialNumberForm, "RegisterForm": registerForm})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('users-home')

# class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
#     template_name = 'users/change_password.html'
#     success_message = "Successfully Changed Your Password"
#     success_url = reverse_lazy('users-home')

@login_required
def ChangePasswordView(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'users/change_password.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})
