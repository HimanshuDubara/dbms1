# Generated by Django 3.0.6 on 2020-05-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('TeamID', models.IntegerField(primary_key=True, serialize=False)),
                ('TeamName', models.CharField(max_length=50)),
                ('TeamRank', models.IntegerField()),
            ],
        ),
    ]
