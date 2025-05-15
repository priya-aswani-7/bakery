from django.views.generic import ListView, CreateView, DetailView, EditView, DeleteView
from django.utils import reverse_lazy
from models import Cake, Customer

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
    success_url=reverse_lazy('cake_list')

# edit cake 
class CakeEditView(EditView):
    model=Cake
    template_name='./cakes/cake_form.html'
    context_object_name='cake'
    success_url=reverse_lazy('cake_detail')
    
# delete cake
class CakeDeleteView(DeleteView):
    model=Cake
    template_name='./cakes/cake_confirm_delete.html'
    context_object_name='cake'
    success_url=reverse_lazy('cake_list')