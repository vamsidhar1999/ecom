from ecom.models import Product,CartItem
from django.shortcuts import get_object_or_404
from django.db.models import Sum
import uuid

def cart_id_(request):
	if 'cart_id' not in request.session:
		request.session['cart_id'] = str(uuid.uuid4())
	return request.session['cart_id']

def get_cart_items(request):
	return CartItem.objects.filter(cart_id = cart_id_(request))


def add_to_cart(request):
	quantity = request.form_data['quantity'] #accessing quantity from form
	product_id = request.form_data['product_id'] #accessing product id from form
	
	p = get_object_or_404(Product, id = product_id) #filtering products with product id / p = Product.objects.filter(id = product_id)
	
	cart_items = get_cart_items(request) #filtering cartitems with cart id

	item_in_cart = False #initializing item

	for i in cart_items: #if product exist in cart, update quantity
		if i.product_id == product_id:
			i.update_quantity(quantity)
			item_in_cart = True

	if not item_in_cart: # if not , add item
		item = CartItem(cart_id = cart_id_(request), price = p.price,quantity = quantity, product_id = product_id)
		item.save() #adding cartitem manually

def item_count(request):
	return get_cart_items(request).aggregate(count = Sum('quantity'))

def total(request):
	cart_items = get_cart_items(request)
	total_ = 0
	for i in cart_items:
		total_ = total_ + i.total_cost()
	return total_