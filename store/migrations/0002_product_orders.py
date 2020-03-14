# Generated by Django 3.0.4 on 2020-03-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orders',
            field=models.ManyToManyField(through='transactions.Ordered', to='transactions.Order'),
        ),
    ]
