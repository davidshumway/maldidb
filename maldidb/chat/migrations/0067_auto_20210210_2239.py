# Generated by Django 3.1 on 2021-02-10 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0066_userfile_spectra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='spectra',
            field=models.ManyToManyField(blank=True, to='chat.Spectra'),
        ),
    ]
