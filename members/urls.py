from django.urls import path
from .views import user_register_view

urlpatterns = [
    path('register/', user_register_view.as_view(), name='register'),
    
]