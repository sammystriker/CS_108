# Generated by Django 3.0.5 on 2020-05-03 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0006_statusmessage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='_profile_friends_+', to='mini_fb.Profile'),
        ),
    ]
