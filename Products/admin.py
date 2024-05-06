from django.contrib import admin
from .models import *

admin.site.register(PhotoServices)
admin.site.register(PhotoClient)
admin.site.register(PhotoProjects)

admin.site.register(Services)

admin.site.register(Projects)
admin.site.register(Clients)
admin.site.register(Social)