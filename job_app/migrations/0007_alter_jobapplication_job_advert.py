# Generated by Django 4.1.2 on 2022-10-27 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0006_jobadvert_status_jobapplication_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='job_advert',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_app.jobadvert'),
        ),
    ]
