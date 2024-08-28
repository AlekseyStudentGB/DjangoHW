from django.urls import path
from . import views
urlpatterns = [
    path('orders/<int:pk>/<int:days>', views.get_orders, name='get_order'),
    path('pr/<int:pk>/<int:days>', views.get_product_in_orders, name='get_pr'),
]
