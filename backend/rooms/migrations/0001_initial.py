# Generated by Django 4.0.6 on 2022-07-17 09:29

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('password', models.CharField(max_length=16, null=True)),
                ('slot', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Slot')),
                ('status', models.CharField(choices=[('WAITING', 'Waiting'), ('IN_PROGRESS', 'In Progress'), ('FINISHED', 'Finished')], default='WAITING', max_length=15, verbose_name='Status Room')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Room created')),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
    ]
