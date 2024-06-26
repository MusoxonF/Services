# Generated by Django 5.0.3 on 2024-05-03 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_alter_social_facebook_alter_social_github_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='projects_photo/')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='services_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frontend', models.TextField()),
                ('backend', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255)),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True)),
                ('title_en', models.CharField(blank=True, max_length=255, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('photos', models.ManyToManyField(related_name='Projects_photos', to='Products.photoprojects')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AlterField(
            model_name='services',
            name='photos',
            field=models.ManyToManyField(related_name='services_photos', to='Products.photoservices'),
        ),
    ]
