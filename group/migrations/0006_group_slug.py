# Generated by Django 4.1.7 on 2023-02-23 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0005_alter_group_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]