from django.contrib import admin
from .models import *
from .mixins import ExportAsCSVMixin


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ['product_name', 'price', 'count_product']
    fieldsets = [
        (
            None,
            {
                'classes': '',
                'fields': ['product_name', 'img', 'date_add']
            }

        ),
        (
            'Описание',
            {
                'classes': ['collapse'],
                'description': 'Категория товаров и его описание',
                'fields': ['description']
            }
        ),
    ]
    readonly_fields = ['date_add']
    actions = ['export_csv']


@admin.register(User)
class AdminUser(admin.ModelAdmin,ExportAsCSVMixin):
    list_display = ['user_name', 'email', 'reg_date']
    fieldsets = [
        (
            None,
            {
                'classes': '',
                'fields': ['user_name',  'reg_date']
            }

        ),
        (
            'Контакты',
            {
                'classes': ['collapse'],
                'description': '(Почта, телефон, адрес)',
                'fields': ['email', 'user_phone', 'user_address']
            }
        ),
    ]
    readonly_fields = ['reg_date']
    actions = ['export_csv']

    @admin.register(User)
    class AdminUser(admin.ModelAdmin, ExportAsCSVMixin):
        list_display = ['user_name', 'email', 'reg_date']
        fieldsets = [
            (
                None,
                {
                    'classes': '',
                    'fields': ['user_name', 'reg_date']
                }

            ),
            (
                'Контакты',
                {
                    'classes': ['collapse'],
                    'description': 'Категория товаров и его описание',
                    'fields': ['email', 'user_phone', 'user_address']
                }
            ),
        ]
        readonly_fields = ['date_add']
        actions = ['export_csv']
