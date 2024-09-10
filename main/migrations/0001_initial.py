# Generated by Django 5.1.1 on 2024-09-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('stock', models.PositiveIntegerField(default=0)),
                ('origin', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]