# Generated by Django 2.1.5 on 2019-01-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0008_auto_20190130_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=50),
        ),
    ]
