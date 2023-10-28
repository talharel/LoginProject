from django.conf.urls import url
from LoginApp import views

# Template Urls
app_name = 'LoginApp'

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^register',views.register,name='register'),
    url(r'^userLogin',views.userLogin,name='userLogin'),
]
