# Generated by Django 3.1.3 on 2020-12-03 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_confirmemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='family_type',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='family_values',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
    ]