# Generated by Django 2.2.6 on 2019-10-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_app', '0018_auto_20191016_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graymodel',
            name='gray_image',
            field=models.ImageField(default='output/gray/gray.jpg', upload_to=''),
        ),
    ]
