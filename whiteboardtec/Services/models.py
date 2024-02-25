from django.db import models
import os, uuid


def ServicePic(instance, filepath):
    "Function for Service Picture"
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('service', filename)

class ServiceImage(models.Model):
    caption = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to=ServicePic)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.caption