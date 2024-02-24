from django.db import models


class Contact(models.Model):
    primary = models.CharField(max_length=15)
    secondary = models.CharField(max_length=15, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.primary

class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    objects = models.Manager()

    def __str__(self):
        return self.email

class Address(models.Model):
    location = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    address_line3 = models.CharField(max_length=255, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f"{self.address_line1}, {self.address_line2}, {self.address_line3}"

class Social(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=255)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Connect(models.Model):
    contact = models.ManyToManyField(Contact)
    email = models.ManyToManyField(Email)
    address = models.ManyToManyField(Address)
    social = models.ManyToManyField(Social)
    objects = models.Manager()