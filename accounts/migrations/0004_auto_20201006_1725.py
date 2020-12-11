# Generated by Django 2.2.13 on 2020-10-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0026_labgroup'),
        ('accounts', '0003_auto_20201006_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='lab_group',
        ),
        migrations.AddField(
            model_name='user',
            name='lab_group',
            field=models.ManyToManyField(blank=True, to='chat.LabGroup'),
        ),
    ]
