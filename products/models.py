from django.db import models
from category.models import CategoryModel
# Create your models here.
class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=80)
    desc = models.TextField(max_length=400)
    featured_image = models.ImageField(upload_to="products/images/", blank=True, null=True)
    featured_video = models.FileField(upload_to="products/videos/", blank=True, null=True) 
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(CategoryModel, related_name="products",)

    def __str__(self):
        return self.title;
