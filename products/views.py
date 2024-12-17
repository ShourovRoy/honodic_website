from django.shortcuts import render
from category.models import CategoryModel
from .models import ProductModel
# Create your views here.

def products_view(request):
    categories = CategoryModel.objects.all().order_by("-updated_at")
    products = ProductModel.objects.all().order_by("-updated_at")

    category_id = request.GET.get("category_id")
    
    if category_id:
        category_obj = CategoryModel.objects.get(id=int(category_id))
        products = category_obj.products.all()


    context = {
        "categories": categories,
        "products": products, 
    }

    return render(request, "products/products.html", context)


def product_details_view(request, product_id):

    product_details = ProductModel.objects.get(id=product_id)

    print(product_details.desc)

    context = {
        "product_details": product_details
    }

    return render(request, 'products/product_details.html', context)


