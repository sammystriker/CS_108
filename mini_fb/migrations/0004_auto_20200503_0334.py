# Generated by Django 3.0.5 on 2020-05-03 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0003_auto_20200503_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmessage',
            name='timestamp',
            field=models.TimeField(blank=True),
        ),
    ]