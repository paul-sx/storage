# Generated by Django 3.2.3 on 2021-06-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_auto_20210523_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
