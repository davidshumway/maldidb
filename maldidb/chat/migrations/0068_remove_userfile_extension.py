# Generated by Django 3.1 on 2021-02-10 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0067_auto_20210210_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfile',
            name='extension',
        ),
    ]
