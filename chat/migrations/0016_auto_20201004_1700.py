# Generated by Django 2.2.13 on 2020-10-04 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_auto_20201001_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('PB', 'Public'), ('PR', 'Private')], default='PB', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, max_length=2048)),
                ('privacyLevel', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.PrivacyLevel')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='library',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat.Library'),
            preserve_default=False,
        ),
    ]
