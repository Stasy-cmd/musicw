# Generated by Django 4.0.4 on 2022-07-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_track_logo_alter_track_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
