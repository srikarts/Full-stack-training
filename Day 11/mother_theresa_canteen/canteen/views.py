from django.shortcuts import render, get_object_or_404
from .models import CanteenModel


def product_list(request):
    ob_products = CanteenModel.objects.all()
    return render(request, 'product_list.html', {'products': ob_products})

def product_detail(request, pk):
    ob_product = get_object_or_404(CanteenModel, pk=pk)
    return render(request, 'product_detail.html', {'product': ob_product})
