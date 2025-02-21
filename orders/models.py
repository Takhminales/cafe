from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]
    
    table_number = models.IntegerField()
    items = models.JSONField()  # Список заказанных блюд с ценами
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')
    
    def __str__(self):
        return f"Заказ №{self.id} (Стол {self.table_number})"
