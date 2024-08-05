from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from .views import signinuser

app_name = 'users'

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('logout/', LogoutView.as_view(next_page='quotes:root'), name='logout'),
    path('signin/', signinuser, name='signin'),
]
