# Generated by Django 3.2.6 on 2021-08-27 05:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0054_remove_selleraccount_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='selleraccount',
            name='joined_at',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
    ]
