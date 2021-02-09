# Generated by Django 2.2.13 on 2021-01-05 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0045_labgroup_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collapsedspectra',
            name='created_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='collapsedspectra',
            name='lab_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.LabGroup'),
        ),
        migrations.AlterField(
            model_name='collapsedspectra',
            name='library',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Library'),
        ),
        migrations.AlterField(
            model_name='collapsedspectra',
            name='xml_hash',
            field=models.ForeignKey(blank=True, db_column='xml_hash', on_delete=django.db.models.deletion.CASCADE, to='chat.XML'),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='created_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='lab_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.LabGroup'),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='library',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.Library'),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='xml_hash',
            field=models.ForeignKey(blank=True, db_column='xml_hash', on_delete=django.db.models.deletion.CASCADE, to='chat.XML'),
        ),
    ]
