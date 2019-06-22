from django.urls import path
from . import views

app_name = "course"
urlpatterns = [
    path('enroll/', views.enroll.as_view(), name='enroll')
]
