# Generated by Django 3.2 on 2021-05-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0002_wine_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='details',
            field=models.TextField(null=True),
        ),
    ]