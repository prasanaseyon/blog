# Generated by Django 4.1.2 on 2023-03-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_post_snippet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Drop Boxes'},
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
