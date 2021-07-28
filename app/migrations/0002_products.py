# Generated by Django 3.2.5 on 2021-07-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('fruits', 'fruits'), ('vegetables', 'vegetables'), ('groceries', 'groceries')], max_length=200)),
                ('pic', models.CharField(max_length=200)),
            ],
        ),
    ]