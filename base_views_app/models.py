from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=300)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
