# Generated by Django 4.1.2 on 2022-12-15 14:55

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0009_alter_jobadvert_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobadvert',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]