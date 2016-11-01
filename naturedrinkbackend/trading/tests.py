from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import PaymentMethod,Order,ItemLine
from product import models
class PaymentMethodTest(APITestCase) :

    def setUp(self):
        self.paymentMethod = PaymentMethod.objects.create(type="B",name="1103702001392")

    def test_list_payment_method(self) :
        response = self.client.get('/api/v1/t/method/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,[{'type':'B','name':'1103702001392','is_active':True,'id':self.paymentMethod.id}])

class CartTest(APITestCase) :

    def setUp(self):
        user=User.objects.create(username="A",password="B")
        self.client.credentials(HTTP_AUTHORIZATION="Token "+Token.objects.get(user__username='A').key)
        self.category = models.Category.objects.create(name='Sample',description='Sample')
        self.product = models.Product.objects.create(name='P',description='PP',price=9,category=self.category)

    def test_add_item_to_cart(self) :
        data = {"product":self.product.id,"quantity":10}
        response = self.client.post('/api/v1/t/cart/',data,format="json")
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
