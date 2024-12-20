from django.shortcuts import render
from .models import HomeAboutContent, HomeSliderContent, HomeUniqueFeature, HomeFeaturedProductDetail
from products.models import Product

# Create your views here.
def HomeView(request):
    sliders =  HomeSliderContent.objects.all()
    about_information =  HomeAboutContent.objects.get()
    unique_features = HomeUniqueFeature.objects.all()
    featured_product_details = HomeFeaturedProductDetail.objects.get()

    # featured products
    featured_product_list = Product.objects.all().filter(is_featured=True).order_by("updated_at")[:4]

    context = {
        "sliders": sliders, 
        "about_information": about_information, 
        "unique_features": unique_features, 
        "featured_product_list": featured_product_list,
        "featured_product_details": featured_product_details, 
    }

    return render(request, 'home/home.html', context)

