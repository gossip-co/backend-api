# Generated by Django 4.1.7 on 2023-02-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_group_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
