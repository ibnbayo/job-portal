# Generated by Django 4.1.2 on 2022-10-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0004_jobadvert_is_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobadvert',
            name='slug',
            field=models.SlugField(default='job'),
        ),
    ]
