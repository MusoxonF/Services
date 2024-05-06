"""
URL configuration for Service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from Products.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('Services/', ServicesView.as_view(), name='services'),
    path('Services/<int:id>/', ServicesDetail.as_view(), name='services_detail'),
    path('ServicesPhotos/', PhotoView.as_view(), name='ServicePhotos'),
    path('ServicesPhotos/<int:id>/', PhotoDetail.as_view(), name='ServicesPhotoDetail'),

    path('Products/', ProductsView.as_view(), name='products'),
    path('Products/<int:id>/', ProductsDetail.as_view(), name='products_detail'),
    path('ProductsPhotos/', PhotoProductView.as_view(), name='ProductPhotos'),
    path('ProductsPhotos/<int:id>/', PhotoProductDetail.as_view(), name='ProductPhotoDetail'),

    path('Projects/', ProjectsView.as_view(), name='projects'),
    path('Projects/<int:id>/', ProjectsDetail.as_view(), name='projects_detail'),
    path('ProjectsPhotos/', PhotoProjectsView.as_view(), name='ProjectPhotos'),
    path('ProjectsPhotos/<int:id>/', PhotoProjectsDetail.as_view(), name='ProjectPhotoDetail'),

    path('Clients/', ClientsView.as_view(), name = 'clients'),
    path('Clients/<int:id>/', ClientsDetail.as_view(), name = 'clients_detail'),
    path('ClientsPhotos/', PhotoClientView.as_view(), name='PhotosClient'),
    path('ClientsPhotos/<int:id>/', PhotoClientDetail.as_view(), name='PhotoClientDetail'),

    path('Social/', SocialView.as_view(), name='social'),
    path('Social/<int:id>/', SocialDetail.as_view(), name = 'social_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)