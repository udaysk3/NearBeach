# Generated by Django 2.1 on 2018-11-10 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0002_initialise_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object_permission',
            name='user_id',
        ),
    ]
