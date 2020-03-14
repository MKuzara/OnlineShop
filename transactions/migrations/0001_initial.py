# Generated by Django 3.0.4 on 2020-03-08 16:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('name_and_surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=350)),
                ('phone_number', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only numbers allowed')])),
                ('shipping_address', models.TextField(max_length=500)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('payment_type', models.PositiveIntegerField(choices=[(1, 'Card'), (2, 'Blik'), (3, 'Transfer'), (4, 'Paypal')])),
                ('shipping_type', models.PositiveIntegerField(choices=[(1, 'Post'), (2, 'Courier'), (3, 'Parcel locker'), (4, 'Own pickup')])),
            ],
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='transactions.Ordered', to='store.Product'),
        ),
    ]
