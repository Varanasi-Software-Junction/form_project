from django.contrib import admin
from django.urls import path
from form_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
    path('custom_contact/', views.custom_contact_view, name='custom_contact'),
]
