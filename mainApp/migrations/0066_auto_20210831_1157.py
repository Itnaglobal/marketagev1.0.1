# Generated by Django 3.2.6 on 2021-08-31 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0065_auto_20210831_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='num_of_pages',
        ),
        migrations.RemoveField(
            model_name='package',
            name='revision',
        ),
        migrations.AddField(
            model_name='package',
            name='num_of_pages_for_basic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_of_pages_for_basic', to='mainApp.numberofpage'),
        ),
        migrations.AddField(
            model_name='package',
            name='num_of_pages_for_premium',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_of_pages_for_premium', to='mainApp.numberofpage'),
        ),
        migrations.AddField(
            model_name='package',
            name='num_of_pages_for_standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='num_of_pages_for_standard', to='mainApp.numberofpage'),
        ),
        migrations.AddField(
            model_name='package',
            name='revision_basic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revision_basic', to='mainApp.revision'),
        ),
        migrations.AddField(
            model_name='package',
            name='revision_premium',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revision_premium', to='mainApp.revision'),
        ),
        migrations.AddField(
            model_name='package',
            name='revision_standard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revision_standard', to='mainApp.revision'),
        ),
    ]