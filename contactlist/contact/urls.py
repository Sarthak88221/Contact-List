from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('add-contact/', views.addcontact, name='add-contact'),
    path('profile/<str:pk>', views.contactprofile, name='profile'),
    path('edit-profile/<str:pk>', views.editprofile, name='editprofile'),
    path('delete/<str:pk>', views.deleteprofile, name='delete'),
]
