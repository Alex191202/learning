from django.contrib import admin
from .models import Stock, Currency  # Импортируем модели

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "name", "description", "currency")

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "ticker", "sign")






