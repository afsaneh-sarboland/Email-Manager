# Generated by Django 4.0.2 on 2022-03-01 13:06

from django.db import migrations, models
import emails.validators


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0008_remove_useremailmapped_bcc_remove_useremailmapped_cc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='<function user_directory_path at 0x7f275cd9fa30>/', validators=[emails.validators.validate_file_size]),
        ),
    ]
