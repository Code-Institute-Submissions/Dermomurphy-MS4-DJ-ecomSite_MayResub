# Generated by Django 3.1.7 on 2021-02-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='style',
            field=models.CharField(choices=[('IPA', 'India Pale Ale'), ('LAGER', 'Lager'), ('STOUT', 'Stout'), ('ALE', 'Ale'), ('PORTER', 'Porter'), ('WHEAT', 'Wheat Beer')], max_length=254),
        ),
    ]
