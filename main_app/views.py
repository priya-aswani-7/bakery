from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Cake, Customer, Order, OrderItem

class HomeView(TemplateView):
    template_name = './base.html'

# list view of cakes
class CakeListView(ListView):
    model=Cake
    template_name='./cakes/cake_list.html'
    context_object_name='cakes'

# detailed view of a single cake
class CakeDetailView(DetailView):
    model=Cake
    template_name='./cakes/cake_detail.html'
    context_object_name='cake'
    
# create cake
class CakeCreateView(CreateView):
    model=Cake
    template_name='./cakes/cake_form.html'
    fields='__all__'
    success_url=reverse_lazy('cake_list')

# edit cake 
class CakeUpdateView(UpdateView):
    model=Cake
    template_name='./cakes/cake_form.html'
    context_object_name='cake'
    fields='__all__'
    
    def get_success_url(self):
        return reverse_lazy('cake_detail', kwargs={'pk': self.object.pk})
    
# delete cake
class CakeDeleteView(DeleteView):
    model=Cake
    template_name='./cakes/cake_confirm_delete.html'
    context_object_name='cake'
    success_url=reverse_lazy('cake_list')
    
# list of customers
class CustomerListView(ListView):
    model=Customer
    template_name='./customers/customer_list.html'
    context_object_name='customers'

# detailed view of customer
class CustomerDetailView(DetailView):
    model=Customer
    template_name='./customers/customer_detail.html'
    context_object_name='customer'
    
# create a customer
class CustomerCreateView(CreateView):
    model=Customer
    template_name='./customers/customer_form.html'
    success_url=reverse_lazy('customer_list')
    fields='__all__'

# update a customer
class CustomerUpdateView(UpdateView):
    model=Customer
    template_name='./customers/customer_form.html'
    context_object_name='customer'
    fields='__all__'
    
    def get_success_url(self):
        return reverse_lazy('customer_detail', kwargs={'pk': self.object.pk})
    
# delete a customer
class CustomerDeleteView(DeleteView):
    model=Customer
    template_name='./customers/customer_confirm_delete.html'
    context_object_name='customer'
    success_url=reverse_lazy('customer_list')

# list of orders
class OrderListView(ListView):
    model=Order
    template_name='./orders/order_list.html'
    context_object_name='orders'
    
# view an order in detail
class OrderDetailView(DetailView):
    model = Order
    template_name = './orders/order_detail.html'
    context_object_name = 'order'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context['available_cakes'] = Cake.objects.exclude(
            id__in=order.cakes.all().values_list('id')
        )
        return context    

# create an order
class OrderCreateView(CreateView):
    model=Order
    template_name='./orders/order_form.html'
    fields=['customer']
    
    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})  
    
# update an order
class OrderUpdateView(UpdateView):
    model=Order
    template_name='./orders/order_form.html'
    context_object_name='order'
    fields='__all__'
    
    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})
    
# delete an order
class OrderDeleteView(DeleteView):
    model=Order
    template_name='./orders/order_confirm_delete.html'
    context_object_name='order'
    success_url=reverse_lazy('order_list')
    
def add_cake_to_order(request, order_id, cake_id):
    try:
        order_item = OrderItem.objects.get(order_id=order_id, cake_id=cake_id)
        order_item.quantity += 1
        order_item.save()
    except OrderItem.DoesNotExist:
        OrderItem.objects.create(order_id=order_id, cake_id=cake_id, quantity=1)
        
    return redirect('order_detail', pk=order_id)

def remove_cake_from_order(request, order_id, cake_id):
    try:
        order_item = OrderItem.objects.get(order_id=order_id, cake_id=cake_id)
        
        if(order_item.quantity > 1):
            order_item.quantity -= 1
            order_item.save()
        else:
            order_item.delete()
            
    except OrderItem.DoesNotExist:
        pass
    
    return redirect('order_detail', pk=order_id)