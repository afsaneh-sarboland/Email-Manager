# Generated by Django 4.0.2 on 2022-03-28 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0028_alter_email_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='file_size',
        ),
    ]
