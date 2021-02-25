# Generated by Django 3.1.7 on 2021-02-25 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('country', models.CharField(blank=True, choices=[('UK', 'United Kingdom'), ('IRL', 'Ireland'), ('USA', 'United States'), ('GER', 'Germany')], max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Breweries',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('style', models.CharField(choices=[('IPA', 'India Pale Ale'), ('LAGER', 'Lager'), ('STOUT', 'Stout'), ('ALE', 'Ale'), ('PORTER', 'Porter')], max_length=254)),
                ('description', models.TextField()),
                ('abv', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('ibu', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('brewery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brewery')),
            ],
        ),
    ]