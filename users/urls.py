from unicodedata import name
from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.Registretion.as_view(), name="regis"),
    path('login/', views.NewLoginView.as_view(), name="login"),
    path('users/', views.UserListView.as_view(), name="user_list"),
]