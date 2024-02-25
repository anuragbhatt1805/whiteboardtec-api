from django.db import models
import os, uuid


def JobDescription(instance, filepath):
    "Function for Job Description file upload"
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('career', 'jd', filename)

def Resume(instance, filepath):
    "Function for Resume file upload"
    ext = os.path.splitext(filepath)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join('career', 'resume', filename)


class Job(models.Model):
    "Model for Job"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    job_description = models.FileField(upload_to=JobDescription)
    location = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

class Application(models.Model):
    "Model for Application"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    resume = models.FileField(upload_to=Resume)
    cover_letter = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.name