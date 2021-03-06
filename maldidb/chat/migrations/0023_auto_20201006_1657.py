# Generated by Django 2.2.13 on 2020-10-06 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0022_auto_20201006_1656'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spectra',
            old_name='uploadedBy',
            new_name='createdBy',
        ),
        migrations.AddField(
            model_name='spectra',
            name='privacyLevel',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='chat.PrivacyLevel'),
            preserve_default=False,
        ),
    ]
