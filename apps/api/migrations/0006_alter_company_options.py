# Generated by Django 4.1.2 on 2022-10-16 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_link_github_alter_link_twitter_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={"verbose_name_plural": "Companies"},
        ),
    ]
