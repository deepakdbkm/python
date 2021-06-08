
from django.urls import path

from shop import views
app_name='shop'
urlpatterns = [
path('',views.allproduct,name= 'allproduct'),
 path('<slug:c_slug>/',views.allproduct,name = 'product_by_cat'),
 path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='procatdetail')

]