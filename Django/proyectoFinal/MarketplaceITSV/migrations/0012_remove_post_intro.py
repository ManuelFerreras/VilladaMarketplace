# Generated by Django 4.0.3 on 2022-04-05 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MarketplaceITSV', '0011_remove_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='intro',
        ),
    ]