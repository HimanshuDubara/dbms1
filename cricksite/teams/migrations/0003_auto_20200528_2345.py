# Generated by Django 3.0.6 on 2020-05-28 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_player'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='Page',
            new_name='PAge',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='Pname',
            new_name='PName',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='Ptype',
            new_name='PType',
        ),
    ]