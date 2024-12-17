from django.db import models

# Create your models here.

class HomeHeroContent(models.Model):
    title = models.CharField(max_length=100, default="", null=True)
    desc = models.TextField(max_length=500, default="", null=True)
    button_name = models.CharField(max_length=20, default="Click Me", null=True)
    image = models.ImageField(upload_to="home", null=True) 
    button_url = models.URLField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


# home about content details
class HomeHeroAboutContentModel(models.Model):
    
    title = models.CharField(max_length=100, default="", null=True)
    desc = models.TextField(max_length=300, default="", null=True)
    featured_image = models.ImageField(upload_to="home", null=True, blank=True) 
    video_link = models.URLField(default="",blank=True, null=True)
    video = models.FileField(upload_to="home/videos", blank=True, null=True)
    button_name = models.CharField(max_length=50, default="Click me", null=True)
    button_link = models.URLField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title


class HomeUniqueFeatures(models.Model):
    title = models.CharField(max_length=80)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="home/unique_features/", blank=True, null=True)

    def __str__(self) -> str:
        return self.title







