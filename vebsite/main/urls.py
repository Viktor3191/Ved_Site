from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about, name='about'),
    path('create', views.create, name='create'),
    path('advertising/', views.advertising, name='advertising'),
    path('alternative', views.alternative, name='alternative'),
]