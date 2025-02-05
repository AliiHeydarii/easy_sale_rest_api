from django.urls import path
from . import views

urlpatterns = [
    path('ads/' , views.AdListApiView.as_view() , name='ads'),
    path('ads/<int:pk>/' , views.AdDetailApiView.as_view() , name='ad-detail'),
    path('users/' , views.UserCreateApiView.as_view(), name='create-user'),
    path('users/profile/' , views.ProfileApiView.as_view(), name='profile')
]