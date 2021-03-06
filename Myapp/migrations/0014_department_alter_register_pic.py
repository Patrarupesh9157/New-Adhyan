# Generated by Django 4.0.2 on 2022-03-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0013_register_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('headdepartment', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=13)),
                ('no_of_student', models.IntegerField()),
                ('dep_date', models.DateField(null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('varify', models.BooleanField(default=False)),
                ('reject', models.BooleanField(default=False)),
                ('approve_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo11.png', upload_to='Profile Pic'),
        ),
    ]
