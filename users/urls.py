from django.urls import path
from .import views

app_name = 'users'
urlpatterns = [
    path(' ', views.user, name='user'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]