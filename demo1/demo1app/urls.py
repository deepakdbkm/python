from . import views
from django.urls import path
from demo1 import settings
from django.conf.urls.static import static

urlpatterns = [

    # path('',views.home,name='home'),
    #path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('detail/', views.detail, name='detail'),
    #path('thanks/', views.thanks, name='thanks'),
    #path('',views.demo,name='demo'),
    path('', views.demo, name='demo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL
                          ,document_root=settings.MEDIA_ROOT)
