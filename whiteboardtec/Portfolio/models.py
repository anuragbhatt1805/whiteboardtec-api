from django.db import models
import os, uuid

# Create your models here.
def PortfolioDoc(instance, filepath):
    "Function for Portfolio Document"
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('portfolio', 'docs', filename)

def PortfolioImage(instance, filepath):
    "Function for Portfolio Image"
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('portfolio', 'image', filename)

class Image(models.Model):
    caption = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=PortfolioImage)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.caption

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ManyToManyField(Image)
    document = models.FileField(upload_to=PortfolioDoc)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
