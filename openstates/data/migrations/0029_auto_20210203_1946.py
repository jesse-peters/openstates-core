# Generated by Django 3.0.5 on 2021-02-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0028_auto_20201022_1642"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventagendaitem",
            name="order",
            field=models.PositiveIntegerField(),
        ),
    ]
