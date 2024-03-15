from django.db import models
from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')
    def __str__(self):
        return self.id


class PhotoProduct(models.Model):
    photo = models.ImageField(upload_to='products_photo/')
    def __str__(self):
        return self.id


class PhotoClient(models.Model):
    photo = models.ImageField(upload_to='clients_photo/')
    def __str__(self):
        return self.id


class Services(models.Model):
    photos = models.ManyToManyField(Photo, related_name='services_photos')
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.title_uz


class Products(models.Model):
    photos = models.ManyToManyField(PhotoProduct, related_name='Products_photos')
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.title_uz


class Clients(models.Model):
    photos = models.ManyToManyField(PhotoClient, related_name='Clients_photos')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.title


class Social(models.Model):
    telegram = models.TextField()
    facebook = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    github = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.telegram