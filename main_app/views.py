from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Cake

def home_view(request):
    return render(request, 'base.html')

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