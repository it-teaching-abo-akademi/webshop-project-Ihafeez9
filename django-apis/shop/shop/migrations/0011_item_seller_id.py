# Generated by Django 4.2.3 on 2023-08-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_item_buyer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='seller_id',
            field=models.IntegerField(null=True),
        ),
    ]