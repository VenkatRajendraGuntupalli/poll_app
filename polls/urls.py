from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.create_poll, name='create_poll'),
    path('vote/<poll_id>/', views.vote_poll, name='vote_poll'),
    path('results/<poll_id>/', views.poll_results, name='poll_results'),
]
