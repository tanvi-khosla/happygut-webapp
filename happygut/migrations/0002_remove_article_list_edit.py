# Generated by Django 3.2.8 on 2021-10-26 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happygut', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article_list',
            name='edit',
        ),
    ]
