# Generated by Django 4.1.3 on 2022-11-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_lesson_prof_lesson_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='first_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='prof',
            name='last_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
