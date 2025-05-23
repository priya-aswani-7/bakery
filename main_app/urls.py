from django.urls import path
from .views import (CakeListView, CakeDetailView, CakeCreateView, CakeUpdateView, CakeDeleteView, 
                    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView, HomeView,
                    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
                    add_cake_to_order, remove_cake_from_order, add_rating_for_cake, remove_rating_for_cake
                    )

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
    
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/create', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete', OrderDeleteView.as_view(), name='order_delete'),
    
    path('orders/<int:order_id>/add-cake/<int:cake_id>', add_cake_to_order, name='add_cake_to_order'),
    path('orders/<int:order_id>/remove-cake/<int:cake_id>', remove_cake_from_order, name='remove_cake_from_order'),

    path('customers/<int:customer_id>/add-cake-rating/<int:cake_id>', add_rating_for_cake, name='add_rating_for_cake'),
    path('customers/<int:customer_id>/remove-cake-rating/<int:cake_id>', remove_rating_for_cake, name='remove_rating_for_cake')
]