# Generated by Django 3.2.6 on 2021-09-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0071_offer_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='is_favorite',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
