from django.db import models
from django.utils import timezone


class User_Data(models.Model):
    full_name = models.CharField(max_length=30)
    id_number = models.CharField(max_length=9)
    role = models.CharField(max_length=15)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)

    class Meta:
        ordering = ("full_name", "id_number", "role", "email", "password")


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.CharField(max_length=40)
    unit = models.CharField(max_length=30)
    qty = models.CharField(max_length=30)
    created_by = models.CharField(max_length=30)
    adding_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ("product_name", "category", "brand", "price", "unit", "qty", "created_by", "adding_date")


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    country = models.CharField(max_length=30)

    class Meta:
        ordering = ("supplier_name", "code", "phone", "email", "country")


class Expense(models.Model):
    description = models.CharField(max_length=30)
    reference = models.CharField(max_length=30)
    date = models.DateField()
    price = models.CharField(max_length=40)

    class Meta:
        ordering = ("description", "reference", "date", "price")


class Transfers(models.Model):
    CHOICES = [('Returned', 'Returned'), ('Loaned', 'Loaned'), ('Pending', 'Pending')]
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    to = models.CharField(max_length=40)
    status = models.CharField(max_length=200, choices=CHOICES)
    start_of_loan = models.DateField()
    end_of_loan = models.DateField()
    qyt = models.CharField(max_length=40)

    class Meta:
        ordering = ("product_name", "category", "brand", "to", "status", "start_of_loan", "end_of_loan")


class Finance(models.Model):
    spending = models.CharField(max_length=30)
    budget = models.CharField(max_length=30)

    class Meta:
        ordering = "budget", "spending"


class Purchases(models.Model):
    product_name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    price = models.CharField(max_length=40)
    unit = models.CharField(max_length=30)
    qty = models.CharField(max_length=30)
    supplier = models.CharField(max_length=30)

    class Meta:
        ordering = ("product_name", "brand", "price", "unit", "qty", "supplier")


class ValidId(models.Model):
    id_number = models.CharField(max_length=9)
    role = models.CharField(max_length=15)

    def __str__(self):
        return self.id_number + ',' + self.role
