# Generated by Django 3.2.6 on 2021-08-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.CharField(default='Unknown', max_length=80),
        ),
    ]
