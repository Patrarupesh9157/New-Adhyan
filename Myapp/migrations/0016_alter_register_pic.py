# Generated by Django 4.0.2 on 2022-03-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0015_alter_register_pic_all_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo3.jpg', upload_to='Profile Pic'),
        ),
    ]
