# Generated by Django 3.2.6 on 2021-08-14 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_gig_is_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='delivery_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.deliverytime'),
        ),
    ]