# Generated by Django 4.2.3 on 2023-08-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_cartitem_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='isPriceChange',
            field=models.BooleanField(default=False),
        ),
    ]