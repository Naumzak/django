# Generated by Django 4.1.3 on 2022-11-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPsy', '0004_alter_quests_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='quests',
            name='factor',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
