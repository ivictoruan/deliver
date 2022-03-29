from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('custumers/', views.getCustumers, name='getcustumers'),
    path('custumers/create/', views.createCustumer),
    path('custumers/<str:pk>/update/', views.updateCustumer, name='update'),
    path('custumers/<str:pk>/', views.getCustumer, name='getCustumer'),
    path('custumers/<str:pk>/delete/', views.deleteCustumer, name='delete'),
]