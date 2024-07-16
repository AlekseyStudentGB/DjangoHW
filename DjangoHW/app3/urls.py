from django.urls import path
from . import views
urlpatterns = [
    path('orders/<int:pk>/<int:days>', views.get_orders, name='get_order')
]
