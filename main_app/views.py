from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Cake, Customer, Order, OrderItem
from django.shortcuts import render, redirect, get_object_or_404

class HomeView(TemplateView):
    template_name = 'base.html'

class CakeListView(ListView):
    model = Cake
    template_name = 'cakes/cake_list.html'
    context_object_name = 'cakes'

class CakeDetailView(DetailView):
    model = Cake
    template_name = 'cakes/cake_detail.html'
    context_object_name = 'cake'

class CakeCreateView(CreateView):
    model = Cake
    template_name = 'cakes/cake_form.html'
    fields = '__all__'
    success_url=reverse_lazy('cake_list')

class CakeUpdateView(UpdateView):
    model = Cake
    template_name = 'cakes/cake_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cake_list')

class CakeDeleteView(DeleteView): 
    model = Cake
    template_name = 'cakes/cake_confirm_delete.html'
    success_url = reverse_lazy('cake_list')
    
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers' 
    
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    success_url=reverse_lazy('customer_list')
    fields = '__all__'

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customer_form.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')
    fields = '__all__'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customer_confirm_delete.html'
    context_object_name = 'customer'
    success_url = reverse_lazy('customer_list')

# Order Views

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    fields = ['customer', 'order_date', 'cakes']
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    fields = ['customer', 'order_date', 'cakes']
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    cakes_not_in_order = Cake.objects.exclude(id__in=order.cakes.all().values_list('id', flat=True))
    if request.method == 'POST':
        cake_id = request.POST.get('cake_id')
        quantity = request.POST.get('quantity')
        if cake_id and quantity:
            OrderItem.objects.create(order=order, cake_id=cake_id, quantity=quantity)
            return redirect('order_detail', pk=order.pk)
    return render(request, 'order_detail.html', {
        'order': order,
        'cakes': cakes_not_in_order,
    })

def remove_cake_from_order(request, order_id, cake_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        OrderItem.objects.filter(order=order, cake_id=cake_id).delete()
    return redirect('order_detail', pk=order.pk)
