from rest_framework import generics
from rest_framework.response import Response
from .models import Cart,CartDetail,Order,OrderDetail
from .serializers import CartSerializer,OrderListSerializer,OrderDetailSerializer
from django.contrib.auth.models import User
from products.models import Product


class CartDetailCreateAPI(generics.GenericAPIView):
    def get(self,request,*args,**kwargs):                       # get or create Cart based on user
        user=User.objects.get(username=self.kwargs['username'])                     #we didnt use request.user because the cart can be added without user login
        cart,created=Cart.objects.get_or_create(user=user,status='Inprogress')
        data=CartSerializer(cart).data
        return Response({'cart':data})
    
    def post(self,request,*args, **kwargs):                     # craete or update products in the Cart
        user=User.objects.get(username=self.kwargs['username'])
        product=Product.object.get(id=request.data['product_id'])
        cart=Cart.object.get(user=user,status='Inprogress')
        cart_detail,created=CartDetail.objects.get_or_create(cart=cart,product=product)
        quantity=int(request.data['quantity'])
        cart_detail.quantity=quantity
        cart_detail.total= quantity*product.price
        cart_detail.save()
        return Response({'status':200,'message':'Product Added Successfully'})
    
    def delete(self,request,*args, **kwargs):
        user=User.objects.get(username=self.kwargs['username'])
        product= Product.objects.get(id=request.data['product_id'])
        cart=Cart.objects.get(user=user,status='Inprogress')
        cart_detail=CartDetail.objects.get(cart=cart,product=product)
        cart_detail.delete()
        return Response({'status':200, 'message': 'Product Deleted Successfully'})
        
        