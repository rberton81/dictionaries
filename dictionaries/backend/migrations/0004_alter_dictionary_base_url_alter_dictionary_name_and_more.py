# Generated by Django 4.2.1 on 2023-05-14 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_dictionary_rate_limit_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dictionary",
            name="base_url",
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name="dictionary",
            name="name",
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AddConstraint(
            model_name="dictword",
            constraint=models.UniqueConstraint(
                fields=("value", "origin"), name="unique_word_per_origin"
            ),
        ),
    ]
