from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
