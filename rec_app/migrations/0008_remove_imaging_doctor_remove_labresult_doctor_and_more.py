# Generated by Django 5.2 on 2025-05-08 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rec_app', '0007_alter_prescription_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imaging',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='labresult',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='serviceprocedure',
            name='doctor',
        ),
    ]
