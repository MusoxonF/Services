from rest_framework import serializers

from .models import *


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoProductSer(serializers.ModelSerializer):
    class Meta:
        model = PhotoProduct
        fields = '__all__'


class PhotoClientSer(serializers.ModelSerializer):
    class Meta:
        model = PhotoClient
        fields = '__all__' 


class ServicesSer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'
        read_only_fields = ['photos']
    def update(self, instance, validated_data):
        # instance.photo = validated_data.get('photo', instace.photo)
        instance.title_uz = validated_data.get('title_uz', instance.title_uz)
        instance.title_ru = validated_data.get('title_ru', instance.title_ru)
        instance.title_en = validated_data.get('title_en', instance.title_en)
        instance.description_uz = validated_data.get('description_uz', instance.description_uz)
        instance.description_ru = validated_data.get('description_ru', instance.description_ru)
        instance.description_en = validated_data.get('description_en', instance.description_en)
        a = validated_data.get('photos', None)
        if a:
            for i in a:
                new_photo = Photo.objects.create(photo=i)
                instance.photo.add(new_photo)
        instance.save()
        return instance


class ServicesGetSer(serializers.ModelSerializer):
    photos = PhotoSer(many=True)
    class Meta:
        model = Services
        fields = ('id', 'photos', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en', 'created_at', 'updated_at')


class ProductsSer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        read_only_fields = ['photos']
        def update(self, instance, validated_data):
            # instance.photo = validated_data.get('photo', instace.photo)
            instance.title_uz = validated_data.get('title_uz', instance.title_uz)
            instance.title_ru = validated_data.get('title_ru', instance.title_ru)
            instance.title_en = validated_data.get('title_en', instance.title_en)
            instance.description_uz = validated_data.get('description_uz', instance.description_uz)
            instance.description_ru = validated_data.get('description_ru', instance.description_ru)
            instance.description_en = validated_data.get('description_en', instance.description_en)
            a = validated_data.get('photos', None)
            if a:
                for i in a:
                    new_photo = PhotoProduct.objects.create(photo=i)
                    instance.photo.add(new_photo)
            instance.save()
            return instance


class ProductsGetSer(serializers.ModelSerializer):
    photos = PhotoProductSer(many=True)
    class Meta:
        model = Products
        fields = ('id', 'photos', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en', 'created_at', 'updated_at')


class ClientsSer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
        read_only_fields = ['photos']
        def update(self, instance, validated_data):
            # instance.photo = validated_data.get('photo', instace.photo)
            instance.title = validated_data.get('title', instance.title)
            a = validated_data.get('photos', None)
            if a:
                for i in a:
                    new_photo = PhotoClient.objects.create(photo=i)
                    instance.photo.add(new_photo)
            instance.save()
            return instance


class ClientsGetSer(serializers.ModelSerializer):
    photos = PhotoClientSer(many=True)
    class Meta:
        model = Clients
        fields = ('id', 'photos', 'title', 'created_at', 'updated_at')


class SocialSer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
