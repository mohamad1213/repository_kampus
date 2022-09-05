from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .forms import *
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from .models import *

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				group = Group.objects.get(name='user') 
				user.groups.add(group)

				return redirect('/accounts/')
			else:
				print(form.errors)
		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home:home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/accounts/')

# def password_reset_request(request):
# 	get_username = User.objects.filter(id=request.user)
# 	print(get_username)
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			password_reset_form.cleaned_data['username']
# 			password_reset_form.save()
# 			return redirect('/reset_password/')
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="admin/accounts/password/password_reset.html",
# 					context={"password_reset_form": password_reset_form})


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['username']
            return redirect("/reset_password_done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form": password_reset_form})