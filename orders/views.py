from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Order
from .forms import OrderForm
from .services import create_order, update_order, delete_order, get_orders_by_status, get_orders_by_table_number, calculate_total_revenue

def order_list(request):
    """Список всех заказов."""
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_create(request):
    """Создание нового заказа."""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            table_number = form.cleaned_data['table_number']
            items = form.cleaned_data['items']
            order = create_order(table_number, items)
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_update(request, order_id):
    """Изменение существующего заказа."""
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            table_number = form.cleaned_data['table_number']
            items = form.cleaned_data['items']
            status = form.cleaned_data.get('status', None)
            updated_order = update_order(order.id, table_number, items, status)
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def order_delete(request, order_id):
    """Удаление заказа по ID."""
    try:
        delete_order(order_id)
    except Order.DoesNotExist:
        raise Http404("Заказ не найден.")
    return redirect('order_list')

def order_search_by_status(request):
    """Поиск заказов по статусу."""
    status = request.GET.get('status', '')
    orders = get_orders_by_status(status)
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_search_by_table_number(request):
    """Поиск заказов по номеру стола."""
    table_number = request.GET.get('table_number', '')
    orders = get_orders_by_table_number(table_number)
    return render(request, 'orders/order_list.html', {'orders': orders})

def total_revenue(request):
    """Выручка за смену (по статусу 'оплачено')."""
    revenue = calculate_total_revenue()
    return render(request, 'orders/total_revenue.html', {'revenue': revenue})
