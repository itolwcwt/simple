# Generated by Django 2.0 on 2019-10-24 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20191024_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='mybody',
        ),
    ]
