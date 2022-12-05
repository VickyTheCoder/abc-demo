from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=18)
    email = models.EmailField()
    company_name = models.CharField(max_length=50)
    tax_number = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=500)