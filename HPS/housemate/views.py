from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, registerForm,landlordRegisterForm,userEditForm,profileEditForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import Group, User

from housemate.hps_logger import *
logger = Logger.instance()

def index(request):
    logger.log("Front page requested")
    return render(request, "housemate/index.html")

def user_login(request):
    # if we add request.method=='POST' is it a bug? i dont know..
    if request.method:
        form = LoginForm(request.POST)
        if form.is_valid():
            cleandata = form.cleaned_data
            #  Authenticate checks if credentials exists in db
            user=authenticate(username=cleandata['username'],
                              password=cleandata['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/housemate")
                else:
                    return HttpResponseRedirect("/housemate")
            else:
                return HttpResponse("Invalid login")
        else:
            form=LoginForm()
        return render(request, 'registration/login.html',{'form':form})


def admin_login(request):
    # if you add request.method=='POST'
    if request.method:
        form = LoginForm(request.POST)
        if form.is_valid():
            cleandata=form.cleaned_data
            user=authenticate(username=cleandata['username'],
                              password=cleandata['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/housemate")
                else:
                    return HttpResponseRedirect("/housemate")
            else:
                return HttpResponse("Invalid login")
        else:
            form=LoginForm()
            return render(request, 'registration/login.html',{'form':form})
        return render(request, 'registration/dashboard.html',{'form':form})
    
# checks if user is authenticated
@login_required
def myboard(request):
    return render(request, 'accounts/dashboard.html', {'section': 'myboard'})




#def register(request):
#    if request.method == "POST":
#        user_form = registerForm(request.POST)
#    return render(request, 'accounts/mydashboard.html', {'section': 'myboard'})


def register(request):
    if request.method:
        user_form=registerForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile=Profile.objects.create(user=new_user) # creates a blank profile
            new_user.groups.add(Group.objects.get(name='tenant'))
            return render(request, 'registration/register_done.html')
        else:
            return render(request, 'registration/register.html', {
                "form": user_form
            })
    return render(request, 'registration/register.html', {
        "form": registerForm()
    })

def registerLandlord(request):
    if request.method == "POST":
        landlord_form=landlordRegisterForm(request.POST)
        if landlord_form.is_valid():
            new_landlord=landlord_form.save(commit=False)
            new_landlord.set_password(landlord_form.cleaned_data['password'])
            new_landlord.is_active=True    
            new_landlord.save()
            profile=Profile.objects.create(user=new_landlord)     # creates a blank profile
            new_landlord.groups.add(Group.objects.get(name='landlord'))
            return render(request, 'registration/register_done.html',{'new_landlord':new_landlord})
        else:
            return render(request, 'registration/landlord_register.html', {
                "form": landlord_form
            })
    return render(request, 'registration/landlord_register.html', {
        'form': landlordRegisterForm()
        })

@login_required
def edit(request):
    if request.method=='POST':
        user_form=userEditForm(instance=request.user, data=request.POST)
        profile_form=profileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated succesfilly')
            return render(request, 'registration/success.html')
        else:
            messages.error(request, 'Error updating profile')
            return render(request, 'accounts/edit.html', {
                "form": user_form
            })

    else:
        user_form=userEditForm(instance=request.user)
        profile_form=profileEditForm(instance=request.user.profile)
    return render(request, 'accounts/edit.html',
                  {'user_form':user_form,
                   'profile_form':profile_form})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='landlords'),login_url='/housemate')
def profile_view(request, user_id):
    my_profile=Profile.objects.get(hm=user_id)
    return render(request, 'accounts/profile.html',{'my_profile':my_profile})


def profile_view_2(request, username):
    my_profile=User.objects.get(username=username)
    y=my_profile.id
    myP=Profile.objects.get(id=y)
    return render(request, 'accounts/profile.html',{'my_profile':myP})
