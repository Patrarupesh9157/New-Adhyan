# Generated by Django 4.0.2 on 2022-04-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0023_alter_add_index_material_alter_register_pic_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo10.png', upload_to='Profile Pic'),
        ),
    ]