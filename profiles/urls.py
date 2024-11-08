from django.urls import path
from . import views 

urlpatterns = [
    path('user_register/', views.user_register, name="user_register"), 
    path('user_login/', views.user_login, name="user_login"), 
    path('user_logout/', views.user_logout, name="user_logout"), 
    path('user_profile/', views.user_profile, name="user_profile"), 
    path('change_pass/', views.change_pass, name="change_pass"), 
    path('change_pass_with_OldPass/', views.change_pass_with_OldPass, name="change_pass_with_OldPass"), 
]
