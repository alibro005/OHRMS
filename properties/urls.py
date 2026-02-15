from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('create/', views.property_create, name='property_create'),
    path('update/<int:pk>/', views.property_update, name='property_update'),
    path('delete/<int:pk>/', views.property_delete, name='property_delete'),

]
