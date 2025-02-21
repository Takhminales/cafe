from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('update/<int:order_id>/', views.order_update, name='order_update'),
    path('delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('search/status/', views.order_search_by_status, name='order_search_by_status'),
    path('search/table/', views.order_search_by_table_number, name='order_search_by_table_number'),
    path('revenue/', views.total_revenue, name='total_revenue'),
]
