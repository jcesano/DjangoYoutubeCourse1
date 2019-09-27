from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places =2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=True)

    def get_absolute_url(self):
        return "/products/{{self.id}}/"


class TransactionHeader(models.Model):
    transac_header_date = models.DateField(default = datetime.now())
    transac_header_name = models.CharField(max_length=50)
    transac_header_total_amount = models.DecimalField(decimal_places =2, max_digits=10000)    
    
class TransactionDetail(models.Model):
    header = models.ForeignKey(TransactionHeader, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    prod_name = models.CharField(max_length=100)
    transac_detail_price = models.DecimalField(decimal_places =2, max_digits=10000)    
    transac_quantity = models.IntegerField();  

