from django.db import models

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
