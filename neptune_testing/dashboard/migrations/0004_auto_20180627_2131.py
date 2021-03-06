# Generated by Django 2.0.2 on 2018-06-28 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180627_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='dashboard.List'),
        ),
        migrations.AlterField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
