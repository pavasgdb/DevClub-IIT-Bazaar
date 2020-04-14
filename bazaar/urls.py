from django.urls import path
from . import views as bazaar_views
from users import views as users_views
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
	path('', bazaar_views.HomePageOptions, name='HomePageOptions'),
	path('Sales/', ProductListView.as_view(), name='HomePageSales'),
	path('About/', bazaar_views.about, name='About'),
	path('Auctions/', bazaar_views.HomePageAuctions, name='HomePageAuctions'),
	path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/buy/', bazaar_views.buyProduct, name='product-buy'),
    # path('product/<int:pk>/buy1/', bazaar_views.buyProduct, name='buyProduct'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]
