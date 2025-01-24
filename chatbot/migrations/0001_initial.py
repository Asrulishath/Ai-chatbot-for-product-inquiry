# Generated by Django 5.1.5 on 2025-01-24 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_info', models.TextField()),
                ('product_categories_offered', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='chatbot.supplier')),
            ],
        ),
    ]
