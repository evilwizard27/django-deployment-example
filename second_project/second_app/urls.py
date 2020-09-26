from django.conf.urls import url
from second_app import views

app_name = 'second_app'

urlpatterns = [
    url('registration/',views.registration,name='registration'),
    url('user_login/',views.user_login,name='user_login'),
    url('user_logout/',views.user_logout,name='user_logout'),
]
