# Generated by Django 2.1.7 on 2019-06-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_tag_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='category',
            field=models.PositiveIntegerField(choices=[(1, 'Style de musique'), (2, 'Type de performance'), (3, 'Ambiance')]),
        ),
    ]
