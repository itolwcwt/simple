# Generated by Django 2.0 on 2019-10-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20191017_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
    ]
