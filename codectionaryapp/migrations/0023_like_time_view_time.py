# Generated by Django 4.1.5 on 2023-01-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codectionaryapp', '0022_like_liker'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='view',
            name='time',
            field=models.DateField(auto_now=True),
        ),
    ]
