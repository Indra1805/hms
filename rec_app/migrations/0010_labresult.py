# Generated by Django 5.2 on 2025-05-09 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_app', '0009_delete_labresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(choices=[('vitals', 'Vitals'), ('lab_results', 'Lab Results'), ('imaging', 'Imaging'), ('prescription', 'Prescription'), ('services_procedures', 'Services & Procedures')], max_length=50)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('patient_id', models.CharField(max_length=100)),
                ('patient_name', models.CharField(max_length=255)),
                ('requested_test', models.CharField(max_length=255)),
                ('requested_by', models.CharField(max_length=255)),
                ('request_date', models.DateField()),
                ('priority', models.CharField(choices=[('Urgent', 'Urgent'), ('Normal', 'Normal')], default='pending', max_length=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('inprogress', 'In Progress'), ('Completed', 'Completed')], default='pending', max_length=15)),
                ('notes', models.TextField(blank=True, null=True)),
                ('user_id', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=150)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('test_time', models.TimeField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('test_type', models.CharField(blank=True, max_length=100, null=True)),
                ('flag', models.BooleanField(default=False)),
                ('report', models.FileField(blank=True, null=True, upload_to='reports/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
