# Generated by Django 3.2.6 on 2021-08-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0032_extendeduser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
