# Generated by Django 4.0.2 on 2022-03-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0023_alter_filter_sender_alter_filter_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter',
            name='sender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filter',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
