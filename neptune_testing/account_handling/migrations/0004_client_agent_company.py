# Generated by Django 2.0.2 on 2018-06-10 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_handling', '0003_agent_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='agent_company',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]