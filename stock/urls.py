from django.urls import path

from stock.views import stock_list, stock_detail, stock_buy, stock_sell, account

app_name = 'stock'  # Убедитесь, что это указано

urlpatterns = [
    path('list/', stock_list, name='list'),
    path('detail/<int:pk>/', stock_detail, name='detail'),
    path('buy/<int:pk>/', stock_buy, name='buy'),
    path('sell/<int:pk>/', stock_sell, name='sell'),  # Новый URL для продажи
    path('account/', account, name='account')
]

