# Generated by Django 4.1.2 on 2022-10-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField()),
                ('linkedin_url', models.CharField(max_length=100)),
                ('github_url', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=200, null=True)),
                ('years_of_experience', models.CharField(choices=[('0', '0-1'), ('1', '1-2'), ('3', '3-4'), ('5', '5-6'), ('7', '7 and above')], default='0', max_length=1)),
                ('cover_letter', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
