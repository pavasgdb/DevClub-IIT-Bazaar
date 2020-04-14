from django.shortcuts import render, redirect, get_object_or_404
from .models import SaleProduct, AuctionProduct
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone
from .forms import ProductBuyForm
from django.http import JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def HomePageOptions(request):
	return render(request, 'bazaar/HomePageOptions.html', {})

def HomePageSales(request):
    context = {
        'SaleProduct': SaleProduct.objects.all()
    }
    return render(request, 'bazaar/HomePageSales.html', {})

def HomePageAuctions(request):
	return render(request, 'bazaar/HomePageAuctions.html', {})

class ProductListView(ListView):
    model = SaleProduct
    template_name = 'bazaar/HomePageSales.html'
    context_object_name = 'SaleProduct'
    ordering = ['-date_available']


class ProductDetailView(DetailView):
    model = SaleProduct


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = SaleProduct
    fields = ['title', 'description','price']

    def form_valid(self, form):
        userm = self.request.user
        username = userm.username
        form.instance.seller = userm
        form.instance.date_available = timezone.now()
        return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = SaleProduct
    fields = ['title', 'description', 'price']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SaleProduct
    template_name = 'bazaar/product_delete.html'
    success_url = '/Sales'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.seller:
            return True
        return False

# def buyProduct(request, pk):
#     if request.method == 'POST':
#         form = ProductBuyForm(request.POST)
#         if form.is_valid():
#             return redirect('HomePageSales')
#     else:
#         form = ProductBuyForm()
#     product = get_object_or_404(SaleProduct,pk=pk)
#     context = {
#         'form': form,
#         'product': product
#     }
#     return render(request, 'baazar/product_buy.html', context)

def ajax_change_status(request):
    active = request.GET.get('active', False)
    job_id = request.GET.get('job_id', False)
    # first you get your Job model
    job = SaleProduct.objects.get(pk=job_id)
    try:
        job.active = active
        job.save()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False})
    return JsonResponse(data)

def buyProduct(request):
    return render(request, 'baazar/product_buy.html', {})

# def buyProduct1(request, pk):
#     return render(request, 'bazaar/product_buy.html', {})

def about(request):
    return render(request, 'bazaar/about.html', {'title': 'About'})