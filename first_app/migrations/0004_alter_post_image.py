# Generated by Django 3.2.12 on 2022-04-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/first_app/media/placeholder.png', upload_to='img'),
        ),
    ]