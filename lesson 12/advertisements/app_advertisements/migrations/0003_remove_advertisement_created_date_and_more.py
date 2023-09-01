# Generated by Django 4.2.3 on 2023-08-04 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='created_date',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
