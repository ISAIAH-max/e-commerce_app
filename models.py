from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    product_category = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return super().__str__()
    
class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=False, blank=False)
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    current_price = models.DecimalField(max_digits=19, decimal_places=2)
    previous_price = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=300)
    
    def __str__(self) -> str:
        return f"ID: {self.id} - Product Name: {self.product_name} - Category: {self.category.product_category} - Description: {self.category.description}"

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=15)
    customer_message = models.TextField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return super().__str__()