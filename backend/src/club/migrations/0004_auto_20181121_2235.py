# Generated by Django 2.1.3 on 2018-11-22 03:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_auto_20181121_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
