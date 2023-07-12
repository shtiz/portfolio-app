# Generated by Django 3.2.10 on 2021-12-21 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('git_url', models.URLField(default=None)),
                ('prev_url', models.URLField(default=None)),
            ],
        ),
    ]