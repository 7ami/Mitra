# Generated by Django 3.0.2 on 2020-01-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20200120_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommo',
            name='img',
            field=models.ImageField(default='', upload_to='media/images'),
        ),
    ]
