# Generated by Django 4.0.4 on 2022-08-06 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_listing_bid_exist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='cond',
            new_name='condition',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='img',
            new_name='image',
        ),
    ]
