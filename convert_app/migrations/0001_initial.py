# Generated by Django 2.2.4 on 2019-09-02 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gray/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('gray_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
