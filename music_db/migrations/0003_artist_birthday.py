# Generated by Django 3.0.5 on 2020-05-06 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_db', '0002_auto_20200505_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='birthday',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]