# Generated by Django 4.2.19 on 2025-02-16 11:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('all_ems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
