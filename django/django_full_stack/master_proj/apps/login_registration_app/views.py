from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
# Create your views here.
def index(request):
    return render(request, "login_registration_app/index.html")

def register(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            print(f'registration info: {request.POST}')
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            print(f'password hashed: {pw_hash}')
            new_user = User.objects.create(first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],email=request.POST['email'],
            password=pw_hash)
            print(f'user created')
            request.session['userid'] = new_user.id
            return redirect(f'/success')
    return redirect(f'/')

def success(request):
    if 'userid' in request.session:
        user = User.objects.get(id = request.session['userid'])
        print(f'logged in user id:{user.id}')
        return render(request, "login_registration_app/welcome.html", {'user': user})
    else:
        return redirect(f'/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                return redirect(f'/success')
            print('bad password')
    return redirect(f'/')

def logout(request):
    request.session.clear()
    return redirect(f'/')

