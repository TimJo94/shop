# Generated by Django 4.0.3 on 2022-04-01 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
