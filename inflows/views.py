from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import forms
from . import models


class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 3

    def get_queryset(self) :
        query_set = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            query_set = query_set.filter(product__title__icontains=product)
        return query_set
    

class InflowCreateView(CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')


class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
