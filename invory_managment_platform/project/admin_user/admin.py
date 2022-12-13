from django.contrib import admin
from admin_user import models


@admin.register(models.User, models.ValidId)
class PlatformUsers(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class Products(admin.ModelAdmin):
    list_display = ("product_name", "category", "brand", "price", "unit", "qty", "created_by")


@admin.register(models.Purchases)
class Purchases(admin.ModelAdmin):
    list_display = ("product_name", "brand", "price", "unit", "qty", "supplier")


@admin.register(models.Finance)
class Finance(admin.ModelAdmin):
    pass


@admin.register(models.Transfers)
class Transfers(admin.ModelAdmin):
    pass


@admin.register(models.Expense)
class Transfer(admin.ModelAdmin):
    pass
