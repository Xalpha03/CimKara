
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_views(request):
    error=False
    message=""
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        user = User.objects.filter(username=username).first()
        if user is not None:
            auth_user = authenticate(username=user.username, password=password)
        
            if auth_user :
                login(request, auth_user)
                return redirect('data:index_name')                
            else:
                message = ("l'utilisateur {} n'est pas authentifié").format(user.username)
        else:
            message = ("Ce nom d'utilisateur {} na pas de compte").format(username)
        
    return render(request, 'Users/login.html', {'message': message})


def logup_views(request):
    logup=False
    message=""
    if request.method == "POST":
        lastname = request.POST.get('lastname', None).upper()
        firstname = request.POST.get('firstname', None).capitalize()
        email = request.POST.get('email', None)
        password1 = request.POST.get('pwd1', None)
        password2 = request.POST.get('pwd2', None)
        username = firstname[0].upper()+lastname.lower()
        print(username)
            
        user = User.objects.filter(Q(username=username)|Q(email=email)).first()
        # print(user.username, user.email)
        
        if user is not None:
        
            if user.username == username:
                message="Cet nom d'utilisateur {} existe déjà!".format(username)
                
            if user.email == email:
                message="Cet email {} existe déjà!".format(email)
        else:
            if len(password1)<6:
                message = "Le mot de passe doit faire au moins 6 caractères!" 
            
            else:
                if password1!= password2:
                    message = "Les mots de passe ne correspondent pas!"
                    
                else:
                    user = User.objects.create_user(last_name=lastname,first_name=firstname,username=username, email=email)
                    user.set_password(password1)
                    if user:
                        logup=True
                        user.save()
                        message= "votre compte a été bien créé et votre nom d'utilisateur est: {}".format(username)
                        return render(request, 'Users/welcome.html', {'message': message, 'logup': logup})
                                    
    return render(request, 'Users/logup.html', {'message': message})


def logout_views(request):
    logout(request)
    return redirect('data:day_name')

# def logup_user_create_views(request):
#     return render(request, 'Users/welcome.html', {})
