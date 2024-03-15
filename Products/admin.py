from django.contrib import admin
from .models import *

admin.site.register(Photo)
admin.site.register(PhotoProduct)
admin.site.register(PhotoClient)

admin.site.register(Services)

admin.site.register(Products)
admin.site.register(Clients)
admin.site.register(Social)