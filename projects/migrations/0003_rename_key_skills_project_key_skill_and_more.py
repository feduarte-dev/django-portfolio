# Generated by Django 4.2.3 on 2024-05-10 15:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="key_skills",
            new_name="key_skill",
        ),
        migrations.RenameField(
            model_name="project",
            old_name="keywords",
            new_name="keyword",
        ),
    ]