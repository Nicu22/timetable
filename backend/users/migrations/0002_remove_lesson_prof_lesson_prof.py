# Generated by Django 4.1.3 on 2022-11-25 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='prof',
        ),
        migrations.AddField(
            model_name='lesson',
            name='prof',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.prof'),
        ),
    ]
