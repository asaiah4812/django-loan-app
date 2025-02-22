# Generated by Django 4.2.9 on 2024-01-21 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debt", "0023_customer_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="Status",
        ),
        migrations.AddField(
            model_name="loan",
            name="Status",
            field=models.CharField(
                choices=[
                    ("Rejected", "Rejected"),
                    ("Pending", "Pending"),
                    ("Approved", "Approved"),
                ],
                default="Pending",
                max_length=50,
                null=True,
            ),
        ),
    ]
