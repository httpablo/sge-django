from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import forms
from . import models


class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 3

    def get_queryset(self) :
        query_set = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            query_set = query_set.filter(product__title__icontains=product)
        return query_set
    

class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
