# Generated by Django 5.0.3 on 2024-03-15 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_clients_created_at_clients_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='facebook',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='github',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='instagram',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='linkedin',
            field=models.TextField(blank=True, null=True),
        ),
    ]
