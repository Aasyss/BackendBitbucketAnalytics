# Generated by Django 2.2.5 on 2019-10-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='change_log_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
