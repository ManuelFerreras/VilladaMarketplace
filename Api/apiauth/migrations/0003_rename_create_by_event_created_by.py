# Generated by Django 3.2.13 on 2022-06-09 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiauth', '0002_event_event_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='create_by',
            new_name='created_by',
        ),
    ]