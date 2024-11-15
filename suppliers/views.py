from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import forms
from . import models


class SupplierListView(ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 3

    def get_queryset(self) :
        query_set = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            query_set = query_set.filter(name__icontains=name)
        return query_set
    

class SupplierCreateView(CreateView):
    model = models.Supplier
    template_name = 'supplier_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')


class SupplierDetailView(DetailView):
    model = models.Supplier
    template_name = 'supplier_detail.html'


class SupplierUpdateView(UpdateView):
    model = models.Supplier
    template_name = 'supplier_update.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(DeleteView):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
