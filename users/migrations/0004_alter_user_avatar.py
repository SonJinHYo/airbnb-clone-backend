# Generated by Django 4.1.5 on 2023-01-11 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]