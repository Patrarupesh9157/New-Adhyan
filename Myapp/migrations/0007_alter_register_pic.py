# Generated by Django 4.0.2 on 2022-03-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0006_delete_all_course_alter_register_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo3.jpg', upload_to='Profile Pic'),
        ),
    ]
