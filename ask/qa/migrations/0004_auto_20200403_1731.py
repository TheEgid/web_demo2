# Generated by Django 3.0.5 on 2020-04-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0003_auto_20200403_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='1078', verbose_name='URL'),
        ),
    ]
