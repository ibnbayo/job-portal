# Generated by Django 4.1.2 on 2022-10-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0005_jobadvert_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobadvert',
            name='status',
            field=models.CharField(choices=[('unpublished', 'Unpublushed'), ('published', 'Published')], default='published', max_length=50),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='cover_letter',
            field=models.TextField(blank=True, default='N/A', max_length=200, null=True),
        ),
    ]