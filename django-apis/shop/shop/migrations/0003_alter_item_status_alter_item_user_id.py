# Generated by Django 4.2.3 on 2023-07-24 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('sale', 'Sale'), ('sold', 'Sold'), ('purchased', 'Purchased')], max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
