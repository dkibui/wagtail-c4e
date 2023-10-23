# Generated by Django 4.2.6 on 2023-10-21 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="FlexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("sub_title", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "verbose_name": "Flex Page",
                "verbose_name_plural": "Flex Pages",
            },
            bases=("wagtailcore.page",),
        ),
    ]