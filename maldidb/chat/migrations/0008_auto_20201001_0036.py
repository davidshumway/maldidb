# Generated by Django 2.2.13 on 2020-10-01 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_auto_20201001_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xml',
            name='analyzer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xml',
            name='detector',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xml',
            name='instrument_metafile',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xml',
            name='ionization',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xml',
            name='manufacturer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xml',
            name='model',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xml',
            name='xml',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='xml',
            name='xml_hash',
            field=models.TextField(blank=True),
        ),
    ]