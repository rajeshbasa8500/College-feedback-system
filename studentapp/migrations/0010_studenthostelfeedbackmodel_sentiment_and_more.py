# Generated by Django 4.0.5 on 2022-07-23 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0009_studentfacultyfeedbackmodel_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenthostelfeedbackmodel',
            name='sentiment',
            field=models.CharField(help_text='sentiment', max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='studenttransportfeedbackmodel',
            name='sentiment',
            field=models.CharField(help_text='sentiment', max_length=80, null=True),
        ),
    ]
