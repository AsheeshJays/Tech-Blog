# Generated by Django 4.0 on 2022-07-05 13:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('TechApp', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('cno', models.AutoField(primary_key=True, serialize=False)),
                ('comment_data', models.TextField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('par', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TechApp.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechApp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]