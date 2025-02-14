# Generated by Django 4.2.9 on 2024-01-21 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debt", "0020_alter_target_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="NationalID",
            field=models.FileField(
                default=datetime.datetime(
                    2024, 1, 21, 16, 14, 9, 638272, tzinfo=datetime.timezone.utc
                ),
                upload_to="Documents/",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="PassportSize",
            field=models.ImageField(
                default=datetime.datetime(
                    2024, 1, 21, 16, 14, 19, 234494, tzinfo=datetime.timezone.utc
                ),
                upload_to="Passports/",
            ),
            preserve_default=False,
        ),
    ]
