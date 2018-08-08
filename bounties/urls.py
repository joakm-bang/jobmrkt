from django.urls import path

from . import views

urlpatterns = [
    path(r'new/', views.create_bounty, name='create_bounty'),
]