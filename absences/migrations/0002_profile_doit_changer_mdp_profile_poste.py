# Generated by Django 5.2.3 on 2025-07-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='doit_changer_mdp',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='poste',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
