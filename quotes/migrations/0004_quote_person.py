# Generated by Django 3.0.5 on 2020-04-21 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20200421_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='person',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotes.Person'),
            preserve_default=False,
        ),
    ]
