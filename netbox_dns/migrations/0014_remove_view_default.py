# Generated by Django 4.0.4 on 2022-04-26 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_dns", "0013_alter_zone_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="view",
            name="default",
        ),
    ]
