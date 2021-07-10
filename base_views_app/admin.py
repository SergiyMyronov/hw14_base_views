from base_views_app.models import City, Customer, Product, Supplier

from django.contrib import admin


class CityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    list_display = ['name', ]
    search_fields = ['name']


class ProductInline(admin.TabularInline):
    model = Product
    extra = 2


class SupplierAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'city']}),
    ]
    inlines = [ProductInline]
    list_display = ['name', 'city', ]
    search_fields = ['name']


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'city', 'products']}),
    ]
    list_display = ['name', 'city']
    list_filter = ['name', 'city']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['code', 'name', 'supplier']}),
    ]
    list_display = ['code', 'name', 'supplier']
    list_filter = ['supplier']
    search_fields = ['name']


admin.site.register(City, CityAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Customer, CustomerAdmin)
