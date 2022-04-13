# Generated by Django 4.0.2 on 2022-04-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
            ],
            options={
                'db_table': 'files',
                'ordering': ['-id'],
            },
        ),
    ]
