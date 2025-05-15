from django.urls import path
from views import (CakeListView, CakeDetailView, CakeCreateView, CakeEditView, CakeDeleteView)

urlpatterns = [
    path('cakes/', CakeListView.as_view(), name='cake_list'),
    path('cakes/create', CakeCreateView.as_view(), name='cake_create'),
    path('cakes/<int:pk>', CakeDetailView.as_view(), name='cake_detail'),
    path('cakes/<int:pk>/edit', CakeEditView.as_view(), name='cake_edit'),
    path('cakes/<int:pk>/delete', CakeDeleteView.as_view(), name='cake_delete')       
]