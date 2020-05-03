from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from ecom.models import Product
from ecom.forms import CartForm
from ecom import cart


# Create your views here.
def index(request):
	p = Product.objects.all()
	context = {'p':p}
	return render(request,'index.html',context)

def show_product(request,product_id,product_slug):
	p = get_object_or_404(Product, id = product_id)

	if request.method == 'POST':
		form = CartForm(request, request.POST)
		if form.is_valid():
			request.form_data = form.cleaned_data
			cart.add_to_cart(request)
			return redirect('ecom:cart')

	form = CartForm(request, initial = {'product_id':product_id})
	context = {'p':p,'form':form}
	return render(request,'detail.html',context)

def show_cart(request):
	if request.method == 'POST':
		item_id = request.POST.get('item_id')
		cart.get_cart_items(request).delete()
	c = cart.get_cart_items(request)
	total = cart.total(request)
	item_count = cart.item_count(request)
	context = {'c':c}
	return render(request,'cart.html',context)

def search(request):
	if request.method == 'GET':
		query = request.GET.get('q')
		s = Product.objects.filter(title__contains = query)
		context = {'s':s}
		return render(request,'search.html',context)
	else:
		return render(request,'search.html')