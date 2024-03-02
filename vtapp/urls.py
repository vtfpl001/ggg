# vtapp/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('certificates/', views.certificates, name='certificates'),
    path('certificates/create/', views.certificate_create, name='certificate_create'),
    path('certificates/<int:pk>/', views.certificate_detail, name='certificate_detail'),
    path('certificates/<int:pk>/update/', views.certificate_update, name='certificate_update'),
    path('certificates/<int:pk>/delete/', views.certificate_delete, name='certificate_delete'),
    path('contact/', views.contact, name='contact'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
