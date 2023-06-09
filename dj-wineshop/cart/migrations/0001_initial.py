# Generated by Django 3.2 on 2021-05-14 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_out', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=1, default=0.0, max_digits=12)),
                ('wines', models.ManyToManyField(blank=True, to='wine.Wine')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=1, default=0.0, max_digits=12)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wine.wine')),
            ],
        ),
    ]
