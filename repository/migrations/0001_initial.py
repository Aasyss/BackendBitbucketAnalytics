# Generated by Django 2.2.5 on 2019-09-18 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.URLField()),
                ('uuid', models.CharField(max_length=50)),
                ('created_on', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('updated_on', models.DateField()),
                ('slug', models.SlugField()),
                ('is_private', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
