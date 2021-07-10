from base_views_app.views import ProductCreateView, ProductDeleteView, ProductDetailView, \
    ProductListView, ProductUpdateView, index, login


from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('prod/', ProductListView.as_view(), name='product_list'),
    path('prod/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('prod/new', ProductCreateView.as_view(), name='product_form'),
    path('prod/edit/<int:pk>', ProductUpdateView.as_view(), name='product_form'),
    path('prod/delete/<int:pk>', ProductDeleteView.as_view()),
    path('login/', login, name='login'),
]
