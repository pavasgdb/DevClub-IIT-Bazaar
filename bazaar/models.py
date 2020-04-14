from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

class SaleProduct(models.Model):
	seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	title = models.CharField(max_length = 100)
	description = models.TextField()
	price = models.IntegerField()
	date_available = models.DateTimeField(default = timezone.now)
	available = models.BooleanField(default = True)
	buyer = models.CharField(max_length = 150, default='')

	def publish(self):
		self.date_available = timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'pk': self.pk})

class AuctionProduct(models.Model):
	seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	title = models.CharField(max_length = 100)
	description = models.TextField(blank = True, null = True)
	maxprice = models.IntegerField()
	customer = models.CharField(max_length = 50)
	available = models.BooleanField()
	date_available = models.DateTimeField(default = timezone.now)
	date_end = models.DateTimeField()

	def publish(self):
		self.date_available = timezone.now()
		self.save()

	def update(self, name, price):
		self.customer = name
		self.maxprice = price

	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'pk': self.pk})