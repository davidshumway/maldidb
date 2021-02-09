# Generated by Django 3.1 on 2021-02-09 04:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0063_merge_20210209_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('start', 'Started'), ('run', 'Running'), ('complete', 'Completed'), ('error', 'Completed - Error'), ('info', 'Info')], max_length=255)),
                ('status_date', models.DateTimeField(auto_now_add=True)),
                ('extra', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='collapsedspectra',
            name='lower_mass_cutoff',
        ),
        migrations.RemoveField(
            model_name='collapsedspectra',
            name='min_SNR',
        ),
        migrations.RemoveField(
            model_name='collapsedspectra',
            name='upper_mass_cutoff',
        ),
        migrations.AddField(
            model_name='collapsedspectra',
            name='min_snr',
            field=models.DecimalField(decimal_places=2, default=0.25, max_digits=4),
        ),
        migrations.AddField(
            model_name='metadata',
            name='library',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.library'),
        ),
        migrations.AlterField(
            model_name='collapsedspectra',
            name='peak_percent_presence',
            field=models.DecimalField(decimal_places=1, default=70.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='collapsedspectra',
            name='tolerance',
            field=models.DecimalField(decimal_places=3, default=0.002, max_digits=10),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='acquisition_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='acquisition_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='acquisition_mode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='acquisition_operator_mode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='cId',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='calibration_constants',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='data_system',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='data_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='digitizer_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='flex_control_version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='ignore',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='inlet',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='instrument',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='instrument_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='instrument_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='ionization_mode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='laser_attenuation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='laser_repetition',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='laser_shots',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='mass_error',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='max_mass',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='min_mass',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='patch',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='spectrometer_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='spectrum_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='spot',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='target_count',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='target_id_string',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='target_serial_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='target_type_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='time_delay',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='time_delta',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='tof_mode',
            field=models.CharField(blank=True, choices=[('REFLECTOR', 'Reflector'), ('LINEAR', 'Linear')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='spectra',
            name='v1_tof_calibration',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_description', models.CharField(blank=True, choices=[('idbac_sql', 'Insert IDBac SQLite data to database'), ('spectra', 'Add spectra files to database'), ('preprocess', 'Preprocess spectra'), ('collapse', 'Collapse replicates'), ('cos_search', 'Cosine score search')], max_length=255, null=True)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('statuses', models.ManyToManyField(to='chat.UserTaskStatus')),
            ],
        ),
        migrations.CreateModel(
            name='UserFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mzml', 'mzxml', 'fid'])])),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('extension', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]