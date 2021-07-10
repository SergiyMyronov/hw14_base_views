from base_views_app.models import Product

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView


def index(request):
    return HttpResponse("Hello, world. You're at the base_views_app index.")


def login(request):
    return HttpResponse("Log in through the admin panel")


class ProductListView(ListView):
    queryset = Product.objects.order_by('name')
    paginate_by = 15


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/base_views_app/login/'
    model = Product
    fields = ['code', 'name', 'supplier']
    success_url = '/base_views_app/prod/'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/base_views_app/login/'
    model = Product
    fields = ['code', 'name', 'supplier']
    success_url = '/base_views_app/prod/'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/base_views_app/login/'
    model = Product
    success_url = '/base_views_app/prod/'
