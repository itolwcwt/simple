# Generated by Django 2.0 on 2019-10-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20191017_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.TextField(default='', max_length=200, verbose_name='显示'),
        ),
    ]