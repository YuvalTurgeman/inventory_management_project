from django.contrib import admin
from admin_user import models


@admin.register(models.ValidId)
class ValidId(admin.ModelAdmin):
    pass

@admin.register(models.User_Data)
class UserData(admin.ModelAdmin):
    list_display = ("full_name", "id_number", "role", "email", "password")


@admin.register(models.Product)
class Products(admin.ModelAdmin):
    list_display = ("product_name", "category", "brand", "price", "unit", "qty", "created_by")


@admin.register(models.Purchases)
class Purchases(admin.ModelAdmin):
    list_display = ("product_name", "brand", "price", "unit", "qty", "supplier")


@admin.register(models.Supplier)
class Supplier(admin.ModelAdmin):
    list_display = ("supplier_name", "code", "phone", "email", "country")


@admin.register(models.Finance)
class Finance(admin.ModelAdmin):
    pass


@admin.register(models.Transfers)
class Transfers(admin.ModelAdmin):
    pass


@admin.register(models.Expense)
class Expense(admin.ModelAdmin):
    pass
