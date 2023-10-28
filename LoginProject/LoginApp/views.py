from django.shortcuts import render
from LoginApp.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'LoginApp/index.html')


def register(request):
    registered = False


    if request.method == 'POST':
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileInfoForm(data=request.POST)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            # hashPass = make_password(user.password) # HASH
            # user.password = hashPass
            # user.save()
            user.set_password(user.password)
            user.save()

            profile = profileForm.save(commit=False)
            profile.user = user # One to one relationship is defined in views with this line

            if 'profilePicture' in request.FILES:
                profile.profilePicture = request.FILES['profilePicture']
            profile.save()

            registered = True

        else:
            print(userForm.errors,profileForm.errors)

    else:
        userForm = UserForm()
        profileForm = UserProfileInfoForm()

    return render(request,'LoginApp/register.html',{'userForm':userForm,'profileForm':profileForm,'registered':registered})


def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                print("aaaa")
                login(request,user)
                return HttpResponseRedirect(reverse('index')) # Send to Index Page

            else:
                return HttpResponse("Account not active")

        else:
            print("Login failed")
            return HttpResponse("Cant Login")

    else:
        return render(request,'LoginApp/login.html')


@login_required
def userLogout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))
