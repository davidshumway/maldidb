# Generated by Django 3.1 on 2021-02-10 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0069_auto_20210210_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertaskstatus',
            name='extra',
            field=models.TextField(blank=True, null=True),
        ),
    ]
