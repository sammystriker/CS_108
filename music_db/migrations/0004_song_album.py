# Generated by Django 3.0.5 on 2020-05-06 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_db', '0003_artist_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='music_db.Album'),
            preserve_default=False,
        ),
    ]
