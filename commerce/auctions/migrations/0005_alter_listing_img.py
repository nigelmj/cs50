# Generated by Django 4.0.4 on 2022-07-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='listing_images'),
        ),
    ]
