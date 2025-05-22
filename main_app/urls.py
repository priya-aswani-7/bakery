from django.urls import path
from .views import (CakeListView, CakeDetailView, CakeCreateView, CakeUpdateView, CakeDeleteView, 
                    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView, HomeView,)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cakes/', CakeListView.as_view(), name='cake_list'),
    path('cakes/create', CakeCreateView.as_view(), name='cake_create'),
    path('cakes/<int:pk>', CakeDetailView.as_view(), name='cake_detail'),
    path('cakes/<int:pk>/update', CakeUpdateView.as_view(), name='cake_update'),
    path('cakes/<int:pk>/delete', CakeDeleteView.as_view(), name='cake_delete'),
    
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/update', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete', CustomerDeleteView.as_view(), name='customer_delete'),
    
    
]