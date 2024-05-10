from rest_framework import serializers

from .models import *


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = PhotoServices
        fields = '__all__'


class PhotoClientSer(serializers.ModelSerializer):
    class Meta:
        model = PhotoClient
        fields = '__all__' 


class PhotoProjectsSer(serializers.ModelSerializer):
    class Meta:
        model = PhotoProjects
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
                new_photo = PhotoServices.objects.create(photo=i)
                instance.photo.add(new_photo)
        instance.save()
        return instance


class ProjectsSer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'
        read_only_fields = ['photos']
        def update(self, instance, validated_data):
            instance.frontend = validated_data.get('frontend', instance.frontend)
            instance.backend = validated_data.get('backend', instance.backend)
            instance.name = validated_data.get('name', instance.name)
            instance.link = validated_data.get('link', instance.link)
            instance.title_uz = validated_data.get('title_uz', instance.title_uz)
            instance.title_ru = validated_data.get('title_ru', instance.title_ru)
            instance.title_en = validated_data.get('title_en', instance.title_en)
            instance.description_uz = validated_data.get('description_uz', instance.description_uz)
            instance.description_ru = validated_data.get('description_ru', instance.description_ru)
            instance.description_en = validated_data.get('description_en', instance.description_en)
            a = validated_data.get('photos', None)
            if a:
                for i in a:
                    new_photo = PhotoProjects.objects.create(photo=i)
                    instance.photo.add(new_photo)
                instance.save()
                return instance


class ProjectsGetSer(serializers.ModelSerializer):
    photos = PhotoProjectsSer(many=True)
    class Meta:
        model = Projects
        fields = ('id', 'photos', 'frontend', 'backend', 'name', 'link', 'title_uz', 'title_ru', 'title_en', 'description_uz', 'description_ru', 'description_en', 'created_at', 'updated_at')



class ServicesGetSer(serializers.ModelSerializer):
    photos = PhotoSer(many=True)
    class Meta:
        model = Services
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


class DevelopersSer(serializers.ModelSerializer):
    class Meta:
        model = Developers
        fields = '__all__'
        def update(self, instance, validated_data):
            instance.fullname = validated_data.get('fullname', instannce.fullname)
            instance.image = validated_data.get('image', instannce.image)
            instance.kasb = validated_data.get('kasb', instance.kasb)
            instance.github = validated_data.get('github', instance.github)
            instance.linkedin = validated_data.get('linkedin', instance.linkedin)
            instance.facebook = validated_data.get('facebook', instance.facebook)
            instance.telegram = validated_data.get('telegram', instance.telegram)
            instance.instagram = validated_data.get('instagram', instance.instagram)
            instance.save()
            return instance
