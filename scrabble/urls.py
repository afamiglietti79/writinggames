from django.urls import path
from . import views

app_name = "scrabble"
urlpatterns = [
    path('response/', views.ScrabbleResponse.as_view(), name='response'),
]
