# Generated by Django 4.1.2 on 2023-02-01 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='subtitle',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Sub título'),
            preserve_default=False,
        ),
    ]
