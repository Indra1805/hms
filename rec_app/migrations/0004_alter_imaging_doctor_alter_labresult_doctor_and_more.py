# Generated by Django 5.2 on 2025-05-06 03:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctoravailability_created_at'),
        ('rec_app', '0003_alter_prescription_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imaging',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imaging', to='doctors.doctoravailability'),
        ),
        migrations.AlterField(
            model_name='labresult',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctoravailability'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='doctors.doctoravailability'),
        ),
        migrations.AlterField(
            model_name='serviceprocedure',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='doctors.doctoravailability'),
        ),
    ]
