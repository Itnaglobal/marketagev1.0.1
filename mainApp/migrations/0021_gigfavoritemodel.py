# Generated by Django 3.2.6 on 2021-08-21 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0020_auto_20210821_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='GigFavoriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_Favorite', models.BooleanField(default=False)),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.gig')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]