from django.contrib import admin
from .models import Order

# Создание класса для настройки отображения модели Order в админке
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_number', 'total_price', 'status')
    list_filter = ('status',)
    search_fields = ('table_number', 'status')
    ordering = ('-id',)

# Регистрация модели Order в админке
admin.site.register(Order, OrderAdmin)
