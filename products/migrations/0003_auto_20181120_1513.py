# Generated by Django 2.1.2 on 2018-11-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181120_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='media',
            field=models.ImageField(null=True, upload_to='articles_pictures/%Y/%m/%d/'),
        ),
    ]
