# Generated by Django 3.1 on 2021-02-09 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0064_auto_20210209_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='extension',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
