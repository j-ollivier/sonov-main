# Generated by Django 2.0.3 on 2018-11-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_tag_is_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]
