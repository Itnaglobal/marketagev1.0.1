# Generated by Django 3.2.6 on 2021-09-05 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0078_auto_20210904_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendoffermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='sendoffermodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]