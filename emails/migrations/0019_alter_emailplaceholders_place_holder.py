# Generated by Django 4.0.2 on 2022-03-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0018_alter_emailreceiver_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailplaceholders',
            name='place_holder',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]