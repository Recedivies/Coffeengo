# Generated by Django 4.0.6 on 2022-07-28 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_userinroom_room_updated_at_room_users_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=16, unique=True, verbose_name='Room Name'),
        ),
    ]
