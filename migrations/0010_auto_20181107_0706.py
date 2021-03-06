# Generated by Django 2.0.3 on 2018-11-07 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0009_auto_20181106_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='SonForBe',
            fields=[
                ('uid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('source_url', models.CharField(max_length=200, verbose_name='URL complète du son')),
                ('source_id_string', models.CharField(max_length=100, verbose_name='Caractères uniques du son')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='static/main/audio', verbose_name='Fichier son')),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='A quelle date le rendre visible')),
                ('posted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='son_author_for_be', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='son',
            name='is_for_be',
        ),
    ]
