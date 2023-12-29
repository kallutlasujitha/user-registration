from django.urls import path
from .import views
urlpatterns = [
    path('',views.SignUp,name='signup'),
    path('login/',views.LogIn,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('delete/<int:user_id>',views.Delete,name='delete'),
    path('home/<int:user_id>',views.Home,name='home'),
    
    
]