from django.db import models
import os, uuid


def GalleryPic(instance, filepath):
    "Function for Gallery Picture"
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('gallery', filename)

class Gallery(models.Model):
    caption = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=GalleryPic)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.caption