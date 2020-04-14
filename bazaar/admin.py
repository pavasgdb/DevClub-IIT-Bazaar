from django.contrib import admin
from .models import SaleProduct, AuctionProduct

admin.site.register(SaleProduct)
admin.site.register(AuctionProduct)