# Generated by Django 4.2.17 on 2025-01-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_channel', '0002_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
