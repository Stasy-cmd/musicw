# Generated by Django 4.0.4 on 2022-07-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_track_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='duration_in_seconds',
            field=models.IntegerField(),
        ),
    ]
