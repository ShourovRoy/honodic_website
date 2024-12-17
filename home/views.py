from django.shortcuts import render
from .models import HomeHeroContent, HomeHeroAboutContentModel, HomeUniqueFeatures
from products.models import ProductModel

# Create your views here.
def HomeView(request):
    sliders =  HomeHeroContent.objects.all()
    about_information =  HomeHeroAboutContentModel.objects.get()
    unique_features = HomeUniqueFeatures.objects.all()

    # featured products
    featured_product_list = ProductModel.objects.all().filter(is_featured=True).order_by("updated_at")[:4]

    context = {
        "sliders": sliders, 
        "about_information": about_information, 
        "unique_features": unique_features, 
        "featured_product_list": featured_product_list
    }

    return render(request, 'home/home.html', context)

