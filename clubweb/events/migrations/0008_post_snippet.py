# Generated by Django 4.1.2 on 2023-03-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click to read', max_length=255),
        ),
    ]