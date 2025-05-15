from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Cake, Customer

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
