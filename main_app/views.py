from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cake

class CakeListView(ListView):
    model = Cake
    template_name = 'cake_list.html'
    context_object_name = 'cakes'

class CakeDetailView(DetailView):
    model = Cake
    template_name = 'cake_detail.html'
    context_object_name = 'cake'

class CakeCreateView(CreateView):
    model = Cake
    template_name = 'cake_form.html'
    fields = '__all__'

class CakeUpdateView(UpdateView):
    model = Cake
    template_name = 'cake_form.html'
    fields = '__all__'
    success_url = reverse_lazy('cake_list')

class CakeDeleteView(DeleteView): 
    model = Cake
    template_name = 'cake_confirm_delete.html'
    context_object_name = 'cake'
    success_url = reverse_lazy('cake_list')