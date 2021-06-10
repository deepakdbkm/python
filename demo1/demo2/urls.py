from . import views
from django.urls import path
from demo1 import settings
from django.conf.urls.static import static
app_name='demo2'
urlpatterns = [


    path('register', views.register, name='reg'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]
