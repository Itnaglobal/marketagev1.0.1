# Generated by Django 3.2.6 on 2021-08-19 11:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0016_gig_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='seller',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
