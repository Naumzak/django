# Generated by Django 4.1.3 on 2022-11-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPsy', '0003_results_rename_answer1_answers_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quests',
            name='number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
