# Generated by Django 4.2.9 on 2024-01-21 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debt", "0029_target_amount_currency_alter_loan_status_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="target",
            name="Amount_currency",
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
                choices=[("Not Active", "Not Active"), ("Active", "Active")],
                default="Active",
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="target",
            name="Amount",
            field=models.FloatField(default=100000),
        ),
    ]
