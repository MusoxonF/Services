from django.db import models


class PhotoServices(models.Model):
    photo = models.ImageField(upload_to='services_photos/')
    def __str__(self):
        return str(self.id)


class PhotoClient(models.Model):
    photo = models.ImageField(upload_to='clients_photo/')
    def __str__(self):
        return str(self.id)


class PhotoProjects(models.Model):
    photo = models.ImageField(upload_to='projects_photo/')
    def __str__(self):
        return str(self.id)


class Services(models.Model):
    photos = models.ManyToManyField(PhotoServices, related_name='services_photos')
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


class Projects(models.Model):
    frontend = models.TextField()
    backend = models.TextField()
    type = models.CharField(max_length=255, null=True, blank=True)
    services = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    photos = models.ManyToManyField(PhotoProjects, related_name='Projects_photos')
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


class Developers(models.Model):
    Jins = [
        ('ayol', 'Ayol'),
        ('erkak', 'Erkak'),
    ]
    fullname = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    kasb = models.CharField(max_length=100)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(choices=Jins, max_length=5)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.fullname
