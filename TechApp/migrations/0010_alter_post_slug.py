# Generated by Django 4.0 on 2022-07-09 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechApp', '0009_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
