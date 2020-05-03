from django.db import models

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length = 100)
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	slug = models.SlugField()
	description = models.TextField()
	img = models.ImageField(upload_to = '')

	def __str__(self):
		return self.title

class CartItem(models.Model):
	product = models.ForeignKey(Product,on_delete = models.PROTECT)
	cart_id = models.CharField(max_length = 30)
	price = models.DecimalField(max_digits = 10, decimal_places = 2)
	quantity = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.product.title

	def update_quantity(self, quantity):
		self.quantity += quantity
		self.save()

	def total_cost(self):
		return self.quantity * self.price