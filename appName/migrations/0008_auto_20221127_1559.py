# Generated by Django 3.2.16 on 2022-11-27 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appName', '0007_auto_20221127_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='next_question_when_no',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='question',
            name='next_question_when_yes',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='question',
            name='solution_when_no',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='question',
            name='solution_when_yes',
            field=models.IntegerField(default=-1),
        ),
    ]
