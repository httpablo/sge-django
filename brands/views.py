from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 3

    def get_queryset(self) :
        query_set = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            query_set = query_set.filter(name__icontains=name)
        return query_set
    

class BrandCreateView(CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'


class BrandUpdateView(UpdateView):
    model = models.Brand
    template_name = 'brand_update.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDeleteView(DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand_list')
