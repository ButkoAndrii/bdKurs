from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('current_query', views.current_query),
]