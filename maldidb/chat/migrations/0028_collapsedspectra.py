# Generated by Django 2.2.13 on 2020-10-22 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0027_cosinescore'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollapsedSpectra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peakPercentPresence', models.DecimalField(decimal_places=2, max_digits=4)),
                ('lowerMassCutoff', models.IntegerField(blank=True)),
                ('upperMassCutoff', models.IntegerField(blank=True)),
                ('minSNR', models.DecimalField(decimal_places=2, max_digits=4)),
                ('tolerance', models.DecimalField(decimal_places=6, default=0.002, max_digits=10)),
                ('spectraContent', models.CharField(choices=[('PR', 'Protein'), ('SM', 'Small Molecule')], default='PR', max_length=2)),
                ('peak_matrix', models.TextField(blank=True)),
                ('spectrum_intensity', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.Library')),
                ('privacy_level', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.PrivacyLevel')),
                ('spectra', models.ManyToManyField(to='chat.Spectra')),
            ],
        ),
    ]
