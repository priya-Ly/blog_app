# Generated by Django 5.0.4 on 2024-04-25 11:58

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
