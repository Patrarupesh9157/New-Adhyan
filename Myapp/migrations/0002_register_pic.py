# Generated by Django 4.0.2 on 2022-03-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='avtar.png', upload_to='Profile Pic'),
        ),
    ]
