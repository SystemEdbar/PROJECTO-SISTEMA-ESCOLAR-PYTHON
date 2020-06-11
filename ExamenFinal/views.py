from django.shortcuts import render
from django.shortcuts import redirect

from Users.RegisterUser import RegisterUser
from Users.FormLoginUser import FormLoginUser

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout


def index(request):
    return render(request, 'Index.html', {
        'message': 'Pagina de Index',
    })


def loginUser(request):
    formLogin = FormLoginUser()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvendio {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usario o Contraseña son invalidos')

    return render(request, 'Users/Login.html', {
        'form': formLogin

    })


def logoutUser(request):
    logout(request)
    messages.success(request, 'Session Cerrada')
    return redirect('loginUser')


def registerUser(request):
    formRegister = RegisterUser(request.POST or None)

    if request.method == 'POST' and formRegister.is_valid():
        user = formRegister.save()
        if user:
            messages.success(request, 'Usuario Creado')
            return redirect('registerUser')
        else:
            messages.error(request, '<Usuario No Creado')
    return render(request, 'Users/registerUser.html', {
        'form': formRegister
    })
