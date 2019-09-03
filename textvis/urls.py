from django.urls import path

from . import views

app_name = "textvis"
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('new/', views.new.as_view(), name='new'),
    path('<int:doc_id>/display/', views.display.as_view(), name='display'),
    path('<int:doc_id>/delete/', views.deleteDoc, name='deletedoc'),
    path('<int:doc_id>/retain/', views.retainDoc, name='retaindoc'),
]
