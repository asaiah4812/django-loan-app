# Generated by Django 4.2.9 on 2024-01-19 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debt", "0015_customer_passport"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="Passport",
        ),
        migrations.AddField(
            model_name="customer",
            name="BusinessType",
            field=models.CharField(
                default=datetime.datetime(
                    2024, 1, 19, 19, 52, 13, 138443, tzinfo=datetime.timezone.utc
                ),
                max_length=250,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="DateOfBirth",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
