# Generated by Django 4.0.2 on 2022-08-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clube',
            name='situation',
            field=models.CharField(default='OnFire', max_length=30),
        ),
    ]