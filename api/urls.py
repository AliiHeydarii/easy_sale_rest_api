from django.urls import path
from . import views

urlpatterns = [
    path('ads' , views.AdListApiView.as_view() , name='ads')
]