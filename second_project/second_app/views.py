from django.shortcuts import render
from second_app.forms import userform,profileform


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'second_app/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('second_app:registration'))

def registration(request):

     registered = False

     if request.method == 'POST':
         user_form = userform(request.POST)
         profile_form = profileform(request.POST)

         if user_form.is_valid() and profile_form.is_valid():

             user = user_form.save()
             user.set_password(user.password)
             user.save()

             profile = profile_form.save(commit=False)
             profile.user = user

             if 'profile_pic' in request.FILES:
                 profile.profile_pic = request.FILES['profile_pic']

             profile.save()
             registered = True

         else:
             print("jatin")


     else:
         user_form = userform()
         profile_form = profileform()

     return render(request,'second_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



def user_login(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        print(user)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS NOT ACTIVE!")
        else:
            return HttpResponse('ACCOUNT IS NOT FIND')
    else:
        return render(request,'second_app/login.html',{})
