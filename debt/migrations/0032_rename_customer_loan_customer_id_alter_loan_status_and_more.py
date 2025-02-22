# Generated by Django 4.2.9 on 2024-01-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debt", "0031_alter_loan_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="loan",
            old_name="Customer",
            new_name="Customer_id",
        ),
        migrations.AlterField(
            model_name="loan",
            name="Status",
            field=models.CharField(
                choices=[
                    ("Rejected", "Rejected"),
                    ("Approved", "Approved"),
                    ("Pending", "Pending"),
                ],
                default="Pending",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="loan",
            name="loanStatus",
            field=models.CharField(
                choices=[("Active", "Active"), ("Not Active", "Not Active")],
                default="Active",
                max_length=50,
                null=True,
            ),
        ),
    ]
