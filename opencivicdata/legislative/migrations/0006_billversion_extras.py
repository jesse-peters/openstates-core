# Generated by Django 2.1a1 on 2018-07-01 22:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('legislative', '0005_auto_20171005_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='billversion',
            name='extras',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
