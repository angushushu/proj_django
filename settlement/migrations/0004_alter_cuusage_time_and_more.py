# Generated by Django 4.0.2 on 2022-07-26 10:30

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('settlement', '0003_alter_maindiag_western_release_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuusage',
            name='time',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=20), default=None, max_length=42, size=2),
        ),
        migrations.AlterField(
            model_name='maindisease',
            name='traditional_release',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main_disease', to='settlement.traditionalrelease'),
        ),
    ]