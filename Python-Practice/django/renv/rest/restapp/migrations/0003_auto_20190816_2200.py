# Generated by Django 2.2.4 on 2019-08-16 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20190816_2158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_created',
            new_name='date_created',
        ),
    ]