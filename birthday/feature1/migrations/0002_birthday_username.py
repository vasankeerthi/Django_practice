# Generated by Django 3.1.2 on 2021-09-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='username',
            field=models.CharField(default='admin', max_length=200),
        ),
    ]