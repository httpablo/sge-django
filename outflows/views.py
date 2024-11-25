from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from app import metrics
from . import forms
from . import models


class OutflowListView(LoginRequiredMixin, ListView):
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context

    
class OutflowCreateView(LoginRequiredMixin, CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')


class OutflowDetailView(LoginRequiredMixin, DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
