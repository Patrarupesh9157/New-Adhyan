# Generated by Django 4.0.2 on 2022-03-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0020_alter_register_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo4.png', upload_to='Profile Pic'),
        ),
    ]
