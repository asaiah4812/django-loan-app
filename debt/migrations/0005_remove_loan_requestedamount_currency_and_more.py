# Generated by Django 5.0.1 on 2024-01-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("debt", "0004_loan_actualdebt_currency_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="loan",
            name="RequestedAmount_currency",
        ),
        migrations.AlterField(
            model_name="loan",
            name="RequestedAmount",
            field=models.FloatField(max_length=8),
        ),
    ]
