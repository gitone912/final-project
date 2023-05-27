from django.urls import path
from .views import index, login_view, register_view, logout_view


urlpatterns = [
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
]
