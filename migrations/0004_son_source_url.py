# Generated by Django 2.0.3 on 2018-04-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20180330_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='son',
            name='source_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
