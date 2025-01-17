# Generated by Django 3.0.5 on 2020-05-06 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_number', models.SmallIntegerField()),
                ('features', models.ManyToManyField(blank=True, to='music_db.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.TextField(verbose_name='Album Name')),
                ('cover', models.ImageField(upload_to='')),
                ('RIAAcerts', models.TextField(choices=[('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Multi-Platinum', 'Multi-Platinum'), ('Diamond', 'Diamond'), ('None', 'None')], default=None)),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_db.Artist')),
            ],
        ),
    ]
