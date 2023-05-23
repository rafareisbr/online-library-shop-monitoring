from django.db import models


class DatetimeTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(DatetimeTracking):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.full_name}  {self.phone}"


class Product(DatetimeTracking):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.name}  {self.price}"


class Transaction(DatetimeTracking):
    customer = models.ForeignKey(
        to="core.Customer", related_name="transactions", on_delete=models.CASCADE)
    product = models.ForeignKey(
        to="core.Product", related_name="transactions", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} at {self.created_at}"
