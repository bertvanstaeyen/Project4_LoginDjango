from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, LoginForm, UpdateUserForm, SerialNumberForm, UpdateMeterNameForm
from .forms import SetPasswordForm
from .models import Profile, SerialNumber, WimhElectricity

# @login_required => user needs to be logged in

# here we are going to create the page and send it to the browser


# home page with graphs of this day
# if user has no serial number -> redirect to add serial number
@login_required
def homeDay(request):
    user = request.user
    profile = user.profile
    numbers = profile.serialnumber_set.all()
    if len(numbers) > 0:
        return render(request, 'users/home-day.html', {'username': user.username})
    else:
        return redirect(to='/serialNumbers/')

# home page with graphs of this week
# if user has no serial number -> redirect to add serial number
@login_required
def homeWeek(request):
    user = request.user
    profile = user.profile
    numbers = profile.serialnumber_set.all()
    if len(numbers) > 0:
        return render(request, 'users/home-week.html', {'username': user.username})
    else:
        return redirect(to='/serialNumbers/')

# home page with graphs of this month
# if user has no serial number -> redirect to add serial number
@login_required
def homeMonth(request):
    user = request.user
    profile = user.profile
    numbers = profile.serialnumber_set.all()
    if len(numbers) > 0:
        return render(request, 'users/home-month.html', {'username': user.username})
    else:
        return redirect(to='/serialNumbers/')

# page to crud serial number
@login_required
def serialNumber(request):
    user = request.user
    profile = user.profile
    numbers = profile.serialnumber_set.all()

    context = {
        'form': SerialNumberForm(),
        'startMessage': False,
        'serial': numbers,
    }

    if len(numbers) < 1:
        context['startMessage'] = True

    if request.method == 'POST':
        form = SerialNumberForm(data=request.POST)
        if form.is_valid():
            print('valid')
            new_serialnumber = form.save(commit=False)
            new_serialnumber.owner_id = request.user.id
            new_serialnumber.save()
            if len(WimhElectricity.objects.filter(serialmeter=new_serialnumber.serialNumber)) > 0:
                messages.success(request, f'Successfully added meter!')
            else:
                messages.warning(request, f'Successfully added meter! But no data was found, make sure the device is connected to your Digital Meter')
            if context['startMessage']:
                return redirect(to='/day/')
            else:
                return redirect(to='/serialNumbers/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    # elif request.method == 'DELETE':
    #     serialNumberId = deleteSerialNumberForm(data=request.DELETE)
    #     SerialNumber.objects.filter(id=serialNumberId).delete()

    return render(request, 'users/crud-serial-number.html', context)
    
# update for the name of the meter
def updateMeterName(request, id):
    serial = SerialNumber.objects.filter(id=id).first()
    if request.method == "POST":
        form = UpdateMeterNameForm(request.POST, instance=serial)
        if form.is_valid():
            serial.save()
            messages.success(request, f'Successfully changed meter name!')
        else:
            messages.error(request, f'Oops, something went wrong!')
    return render(request, 'users/crud-serial-number.html')

# help page for users
# exlpains the app and how to install the device to read the data
def help(request):
    return render(request, 'users/help.html')

# view to register user
class RegisterView(View):
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/day/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # form = self.form_class(initial=self.initial)
        registerForm = RegisterForm(initial=self.initial)
        return render(request, self.template_name, {"RegisterForm": registerForm})

    def post(self, request, *args, **kwargs):

        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():
            registerForm.save()

            username = registerForm.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')
        else:
            for error in list(registerForm.errors.values()):
                messages.error(request, error)

        return render(request, self.template_name, {"RegisterForm": registerForm})


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

# view to change password
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


# view to change username and email
@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        # profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'users/profile.html', {'user_form': user_form})


# delete meter for user, KEEP DATA
@login_required()
def deleteSerialNumber(request, id):
    serialId = SerialNumber.objects.filter(id=id).first()
    if serialId.owner.id == request.user.id:
        if request.method == "POST":
            serialId.delete()
    return render(request, 'users/crud-serial-number.html')

# delete meter for user, WITH DATA
@login_required()
def deleteSerialNumberWithData(request, id):
    serialId = SerialNumber.objects.filter(id=id).first()
    data = WimhElectricity.objects.filter(serialmeter__exact=serialId.serialNumber)
    if serialId.owner.id == request.user.id:
        if request.method == "POST":
            for meter in data:
                meter.delete()
            serialId.delete()

    return render(request, 'users/crud-serial-number.html')
