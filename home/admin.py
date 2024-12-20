from django.contrib import admin
from .models import HomeUniqueFeature, HomeSliderContent, HomeAboutContent, HomeFeaturedProductDetail 

# Register your models here.

admin.site.register(HomeSliderContent)
admin.site.register(HomeAboutContent)
admin.site.register(HomeUniqueFeature)
admin.site.register(HomeFeaturedProductDetail)