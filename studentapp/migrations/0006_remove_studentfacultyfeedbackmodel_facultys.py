# Generated by Django 4.0.5 on 2022-07-15 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_studentfacultyfeedbackmodel_facultys_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentfacultyfeedbackmodel',
            name='facultys',
        ),
    ]
