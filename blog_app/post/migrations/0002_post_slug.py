# Generated by Django 3.0.2 on 2020-02-22 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=70, null='True'),
            preserve_default='True',
        ),
    ]