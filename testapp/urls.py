
from django.urls import path,include
from . import  views 

urlpatterns = [
    path('',views.home),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('success/', views.success),
    path('logout/', views.logout)
 
]