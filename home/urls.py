from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('profileUpdate/', views.profileUpdate.as_view(), name='profileUpdate')
]
