# Generated by Django 3.2 on 2021-05-14 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
