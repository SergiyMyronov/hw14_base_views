import random

from base_views_app.models import City, Customer, Product, Supplier

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    This command is for inserting City, Customer, Product, Supplier into database.
    Inserts all unique rows to City, Supplier, Product. Then inserts Customers.
    """

    help = 'Making some data'  # noqa

    def handle(self, *args, **kwargs):
        City.objects.all().delete()
        Customer.objects.all().delete()
        Product.objects.all().delete()
        Supplier.objects.all().delete()

        cities = 5  # number of cities and suppliers
        products = 60  # number of products (must be more then cities)
        customers = 10  # number of customers (must be less then products)

        cnt = 0
        for c in range(cities):
            city = City.objects.create(name='City'+str(c+1))
            Supplier.objects.create(name='Supplier'+str(c+1), city=city)
            loop = customers // cities
            for i in range(loop):
                Customer.objects.create(name=f'Customer{str(cnt*loop + i + 1).rjust(2, "0")}', city=city)
            cnt += 1

        cnt = 0
        for sup in Supplier.objects.all():
            loop = products // cities
            for i in range(loop):
                Product.objects.create(code=f'Code{str(cnt*loop + i + 1).rjust(2, "0")}',
                                       name=f'Product{str(cnt*loop + i + 1).rjust(2,"0")}', supplier=sup)
            cnt += 1

        cust_all = list(Customer.objects.all())
        prod_all = list(Product.objects.all())
        len_cust_all = len(cust_all)
        len_prod_all = len(prod_all)
        n = len_prod_all // len_cust_all
        for i in range(len_cust_all):
            for b in range(len_cust_all*2):
                cust_all[i].products.add(prod_all[random.randint(0, n-2)*len_cust_all+b])
