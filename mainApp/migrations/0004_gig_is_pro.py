# Generated by Django 3.2.6 on 2021-08-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_gig_pop_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='is_pro',
            field=models.BooleanField(default=False, null=True),
        ),
    ]