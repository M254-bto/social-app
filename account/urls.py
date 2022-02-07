from django.urls import path
from.views import dashboard, register, edit

app_name='account'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit')
]