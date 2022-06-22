from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm



def login_user(request):
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('climbs:home')
        else:
            messages.success(request, ('Incorrect username or password combination.  Please try again.'))
            # context = {'message': 'Incorrect username or password combination.  Please try again.'}
            return redirect('users:login')
    else:
        return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, ('You Were Logged Out.'))
    return redirect('climbs:home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, ("Registration Successfull"))
            return redirect ('climbs:home')
    else:
        form = RegisterUserForm()

    return render(request, 'users/register.html', {
        'form':form,
    })


# def signup(request):
#     context = {}

#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')

#         message = ''
#         if password1 != password2: # the passwords don't match
#             message += 'Passwords do not match.  '
#         if User.objects.filter(username=username).exists(): # the username is already taken
#             message += 'Username already taken.  '
#         if message: # this will run if there are any characters in the message string
#             message += 'Please try again.'
#         else:
#             user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1)
#             login(request, user)
#             return redirect('climbs:home')
#         context = {'message': message}
#     return render(request, 'users/sign_up.html', context)


