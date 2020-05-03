from django.urls import path
from ecom.views import index,show_product,show_cart,search

app_name = 'ecom'

urlpatterns = [
	path('',index,name='index'),
	path('product/<int:product_id>/<slug:product_slug>/',show_product, name= 'detail'),
	path('cart/',show_cart, name = 'cart'),
	path('search/',search,name = 'search'),
	]
