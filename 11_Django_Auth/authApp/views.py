from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home_logout.html')

def home_login(request):
    users = User.objects.values()
    users = list(users)

    users_list = []
    for user in users:
        selected_user = {
            'id': user['id'],
            'username': user['username'],
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email'],
            'is_superuser': user['is_superuser']
        }
        users_list.append(selected_user)

    print(users_list)
    params = {'users': users_list}
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'home_login.html', params)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home_login')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')