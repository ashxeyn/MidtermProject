# Generated by Django 5.1.6 on 2025-02-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_task_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='status',
            field=models.CharField(default='Not Yet Started', max_length=20),
        ),
    ]
