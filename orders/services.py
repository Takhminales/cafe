from .models import Order

def calculate_total_price(items):
    """Функция для вычисления общей стоимости заказа."""
    if not isinstance(items, list):
        raise ValueError("Items should be a list.")
    total_price = sum(item['price'] for item in items)
    return total_price

def create_order(table_number, items):
    """Создание нового заказа с вычислением общей стоимости."""
    total_price = calculate_total_price(items)
    order = Order.objects.create(
        table_number=table_number,
        items=items,
        total_price=total_price,
        status='waiting'
    )
    return order

def update_order(order_id, table_number=None, items=None, status=None):
    """Обновление заказа с возможностью изменения всех полей."""
    order = Order.objects.get(id=order_id)

    if table_number:
        order.table_number = table_number
    if items:
        order.items = items
        order.total_price = calculate_total_price(items)
    if status:
        order.status = status
    
    order.save()
    return order

def delete_order(order_id):
    """Удаление заказа по ID."""
    order = Order.objects.get(id=order_id)
    order.delete()

def get_orders_by_status(status):
    """Получение заказов по статусу."""
    return Order.objects.filter(status=status)

def get_orders_by_table_number(table_number):
    """Получение заказов по номеру стола."""
    return Order.objects.filter(table_number=table_number)

def calculate_total_revenue():
    """Расчет общей выручки по статусу 'оплачено'."""
    paid_orders = Order.objects.filter(status='paid')
    return sum(order.total_price for order in paid_orders)
