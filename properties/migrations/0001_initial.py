# Generated by Django 5.0.7 on 2024-07-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='propertyImage')),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mini_description', models.TextField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('property_type', models.CharField(max_length=20)),
                ('pricing_range', models.CharField(max_length=20)),
            ],
        ),
    ]
