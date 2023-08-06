# Generated by Django 4.2.2 on 2023-08-06 17:24

from django.db import migrations, models
import functions.code_generator


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='code',
            field=models.CharField(default=functions.code_generator.generate_code, max_length=10),
        ),
    ]
