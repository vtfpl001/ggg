
from django.urls import path, include  # Import the 'include' function
from . import views

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    # Registration page.
    path('register/', views.register, name='register'),

]
