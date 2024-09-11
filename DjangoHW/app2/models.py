from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    user_phone = models.CharField(max_length=12)
    user_address = models.CharField(max_length=400)
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'

    def __str__(self):
        return f'id : {self.pk} user_name:{self.user_name} email :{self.email}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, )
    count_product = models.IntegerField()
    date_add = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='products_img/', blank=True)

    class Meta:
        verbose_name: str = 'Продукт'
        verbose_name_plural: str = 'Продукты'

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name: str = 'Заказ'
        verbose_name_plural: str = 'Заказы'

    def __str__(self):
        return f'номер : {self.pk};  customer : {self.customer};  price : {self.total_price}'
