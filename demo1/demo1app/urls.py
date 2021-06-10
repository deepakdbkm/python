from . import views
from django.urls import path
from demo1 import settings
from django.conf.urls.static import static
app_name='demo1app'
urlpatterns = [

    # path('',views.home,name='home'),
    #path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('detail/', views.detail, name='detail'),
    #path('thanks/', views.thanks, name='thanks'),
    #path('',views.demo,name='demo'),
    path('', views.demo, name='demo'),
    path('Home', views.demo, name='demo'),

]

