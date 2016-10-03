from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Address(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    sub_district = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    zipcode = models.PositiveIntegerField(max_length=5,validators=[MinLengthValidator(5)])
