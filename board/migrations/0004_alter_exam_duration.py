# Generated by Django 5.1.2 on 2024-10-20 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0003_alter_answer_question_alter_candidate_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="duration",
            field=models.TimeField(),
        ),
    ]
