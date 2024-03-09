# Generated by Django 4.2.10 on 2024-03-09 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="payment_id",
        ),
        migrations.AddField(
            model_name="payment",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
