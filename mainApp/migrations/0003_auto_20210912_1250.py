# Generated by Django 3.2.6 on 2021-09-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20210912_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.ManyToManyField(blank=True, to='mainApp.Subcategory'),
        ),
    ]
