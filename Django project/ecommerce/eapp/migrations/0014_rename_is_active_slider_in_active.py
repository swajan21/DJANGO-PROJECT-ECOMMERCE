# Generated by Django 4.2.7 on 2024-05-23 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0013_slider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='is_active',
            new_name='in_active',
        ),
    ]