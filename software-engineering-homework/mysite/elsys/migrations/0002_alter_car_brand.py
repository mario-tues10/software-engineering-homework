# Generated by Django 3.2.7 on 2021-09-28 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elsys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=101),
        ),
    ]
