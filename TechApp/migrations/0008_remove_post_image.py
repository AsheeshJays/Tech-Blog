# Generated by Django 4.0 on 2022-07-08 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TechApp', '0007_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
