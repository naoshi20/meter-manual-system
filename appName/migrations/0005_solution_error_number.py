# Generated by Django 3.2.16 on 2022-11-27 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appName', '0004_alter_question_error_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='error_number',
            field=models.IntegerField(default=1),
        ),
    ]
