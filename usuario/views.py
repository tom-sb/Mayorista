from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def authentication(request):
    if request.method == 'POST':
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(username)
        print(password)
        if action == 'login':
            user = authenticate(username=username, password=password)
            
            if user is not None:
            	login(request, user)
                return redirect('usuario:system_index')
        return redirect('usuario:index')



    return render(request, 'login.html', {})

"""
def hello(request):
	return render(request, 'hello.html')
"""