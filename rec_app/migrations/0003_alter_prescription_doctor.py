# Generated by Django 5.2 on 2025-05-05 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec_app', '0002_rename_procedure_name_serviceprocedure_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='rec_app.staffusers'),
        ),
    ]
