from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Animal, Enclosure
from .forms import AnimalForm, EnclosureForm

# Create your views here.


class AnimalListView(ListView):
    model = Animal
    template_name = 'animal_list.html'
    context_object_name = 'animals'

class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animal_detail.html'
    context_object_name = 'animal'

class AnimalCreateView(CreateView):
    model = Animal
    template_name = 'animal_form.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animal_list')

class AnimalUpdateView(UpdateView):
    model = Animal
    template_name = 'animal_form.html'
    form_class = AnimalForm
    success_url = reverse_lazy('animal_list')

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy('animal_list')
    template_name = 'animal_confirm_delete.html'

class EnclosureListView(ListView):
    model = Enclosure
    template_name = 'enclosure_list.html'
    context_object_name = 'enclosures'
    
class EnclosureDetailView(DetailView):
    model = Enclosure
    template_name = 'enclosure_detail.html'
    context_object_name = 'enclosure'

class EnclosureCreateView(CreateView):
    model = Enclosure
    template_name = 'enclosure_form.html'
    form_class = EnclosureForm

    def form_valid(self, form):
        enclosure = form.save(commit=False)
        if enclosure.animals.count() > enclosure.capacity:
            form.add_error(None, "Превышено максимальное количество животных для этого вольера")
            return self.form_invalid(form)
        return super().form_valid(form)
    
    success_url = reverse_lazy('enclosure_list')
    
class EnclosureUpdateView(UpdateView):
    model = Enclosure
    template_name = 'enclosure_form.html'
    form_class = EnclosureForm
    success_url = reverse_lazy('enclosure_list')

class EnclosureDeleteView(DeleteView):
    model = Enclosure
    success_url = reverse_lazy('enclosure_list')
    template_name = 'enclosure_confirm_delete.html'