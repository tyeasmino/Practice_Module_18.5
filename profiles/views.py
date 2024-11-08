from django.shortcuts import render, redirect 
from . import forms  
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash  
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required  


# Create your views here.
def user_register(request):
    if request.method == "POST":
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, "Account Created Successfuly")
            return redirect('user_login')
    else:
        registration_form = forms.RegistrationForm()
    return render(request, 'registration_login.html', {'form': registration_form, 'pageHeading': 'Registraion'})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']

            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful!")
                return redirect('user_profile')
            else:
                messages.info(request, "Login information is not valid!")
                return redirect('user_register')
    else:
        form = AuthenticationForm()

    return render(request, 'registration_login.html', {'form': form, 'pageHeading': 'Login'})



@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'user': request.user})
    else:
        return redirect('user_login')


@login_required
def change_pass(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST ) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed Successfully')
            update_session_auth_hash(request, form.user) 
            return redirect('user_profile')
    else:
        form = PasswordChangeForm(request.user) 

    return render(request, 'change_pass.html', {'form': form})

    
@login_required
def change_pass_with_OldPass(request):
    if request.method == "POST":
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Changed Done')
            update_session_auth_hash(request, form.user)
            return redirect('user_profile')
    
    else: 
        form = SetPasswordForm(request.user)

    return render(request, 'change_pass.html', {'form': form})