# Generated by Django 2.2.13 on 2021-01-02 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201006_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lab_group',
            new_name='lab_name',
        ),
    ]
