# Generated by Django 4.0.4 on 2022-07-06 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('start_bid', models.IntegerField()),
                ('category', models.CharField(blank=True, choices=[('FSH', 'Fashion'), ('ELC', 'Electronics'), ('HME', 'Home'), ('TOY', 'Toys'), ('BOK', 'Books'), ('COL', 'Collectibles')], max_length=3)),
                ('cond', models.CharField(choices=[('BRN', 'Brand New'), ('OPB', 'Open Box'), ('REN', 'Renewed')], default='BRN', max_length=3)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.IntegerField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='auctions.listing')),
            ],
        ),
    ]
