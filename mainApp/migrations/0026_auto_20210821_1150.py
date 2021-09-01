# Generated by Django 3.2.6 on 2021-08-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0025_auto_20210821_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offermanager',
            old_name='Offer',
            new_name='offer',
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('PENDING APPROVAL', 'PENDING APPROVAL'), ('REQUIRED MODIFICATION', 'REQUIRED MODIFICATION'), ('DENIED', 'DENIED'), ('PAUSED', 'PAUSED')], default='ACTIVE', max_length=200, null=True),
        ),
    ]
