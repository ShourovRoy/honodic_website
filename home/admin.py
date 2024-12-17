from django.contrib import admin
from .models import HomeHeroContent, HomeHeroAboutContentModel, HomeUniqueFeatures

# Register your models here.

admin.site.register(HomeHeroContent)
admin.site.register(HomeHeroAboutContentModel)
admin.site.register(HomeUniqueFeatures)