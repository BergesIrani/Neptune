# Generated by Django 2.0.2 on 2018-06-28 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20180627_2131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
        migrations.RemoveField(
            model_name='list',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
