# Generated by Django 4.0.2 on 2022-03-06 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0007_alter_register_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo16.png', upload_to='Profile Pic'),
        ),
        migrations.CreateModel(
            name='All_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coname', models.CharField(max_length=50)),
                ('coduration', models.CharField(max_length=30)),
                ('coprice', models.IntegerField()),
                ('codepartment', models.CharField(max_length=30)),
                ('codiscription', models.TextField(max_length=100)),
                ('coyear', models.IntegerField()),
                ('copic', models.ImageField(default='python.png', upload_to='course pic')),
                ('covarify', models.BooleanField(default=False)),
                ('coreject', models.BooleanField(default=False)),
                ('approve_by', models.CharField(blank=True, max_length=100, null=True)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.register')),
            ],
        ),
    ]
