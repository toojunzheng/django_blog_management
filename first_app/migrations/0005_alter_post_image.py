# Generated by Django 3.2.12 on 2022-04-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
