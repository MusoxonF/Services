# Generated by Django 5.0.3 on 2024-03-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_services_created_at_alter_services_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='photoclient',
            old_name='image',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='photoproduct',
            old_name='image',
            new_name='photo',
        ),
    ]
