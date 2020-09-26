from django.shortcuts import render
from second_app.forms import userform,profileform

# Create your views here.
def index(request):
    return render(request,'second_app/index.html')

def registration(request):

     registered = False

     if request.method == 'POST':
         user_form = userform(request.POST)
         profile_form = profileform(request.POST)

         if user_form.is_valid() and profile_form.is_valid():

             user = user_form.save()
             user.set_password = (user.password)
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

     return render(request,'second_app/registration.html',{})      
