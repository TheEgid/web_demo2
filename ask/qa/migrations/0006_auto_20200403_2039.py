# Generated by Django 3.0.5 on 2020-04-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0005_auto_20200403_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(default=1, verbose_name='URL'),
        ),
    ]
