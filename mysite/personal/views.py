from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from personal.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required



def index(request):
	return render(request, 'personal/home.html')


def contact(request):
	return render(request, 'personal/contact.html', {'content':['Email us on:','nirja.patel11@gmail.com','Call us on:','+1-469-516-2873']})

def register(request):
	if request.method =='POST':
		#form = UserCreationForm(request.POST)
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login')
	else:
		#form = UserCreationForm()
		form = RegistrationForm()
		args = {'form':form}
		return render(request, 'personal/registerForm.html', args)


def profile(request):
	args = {'user': request.user}
	return render(request, 'personal/profile.html', args)

#@login_required
def editprofile(request):
	if request.method == 'POST':
		#form = UserChangeForm(request.POST, instance=request.user)
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/profile')
	else:
		#form = UserChangeForm(instance=request.user)
		form = EditProfileForm(instance=request.user)
		args = {'form':form}
		return render(request, 'personal/editprofile.html', args)

#@login_required
def change_password(request):
	if request.method == 'POST':
		#form = UserChangeForm(request.POST, instance=request.user)
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/profile')
	else:
		#form = UserChangeForm(instance=request.user)
		form = PasswordChangeForm(user=request.user)
		args = {'form':form}
		return render(request, 'personal/editprofile.html', args)


