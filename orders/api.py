from rest_framework import generics
from rest_framework.response import Response
from .models import Cart,CartDetail,Order,OrderDetail
from .serializers import CartSerializer,OrderListSerializer,OrderDetailSerializer
from django.contrib.auth.models import User
from products.models import Product


class CartDetailCreateAPI(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):
        user=User.objects.get(username=self.kwargs['username'])                     #we didnt use request.user because the cart can be added without user login
        cart,created=Cart.objects.get_or_create(user=user,status='Inprogress')
        data=CartSerializer(cart).data
        return Response({'cart':data})
        