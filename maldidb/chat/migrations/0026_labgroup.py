# Generated by Django 2.2.13 on 2020-10-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0025_auto_20201006_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_name', models.TextField()),
            ],
        ),
    ]
