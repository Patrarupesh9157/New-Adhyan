# Generated by Django 4.0.3 on 2022-04-05 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdhyanApp', '0006_rename_users_user'),
        ('Myapp', '0022_all_course_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_index',
            name='material',
            field=models.FileField(upload_to='course pic'),
        ),
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo8.png', upload_to='Profile Pic'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_time', models.DateTimeField(auto_now_add=True)),
                ('pay_type', models.CharField(default='online', max_length=50)),
                ('pay_verify', models.BooleanField(default=False)),
                ('pay_id', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Myapp.all_course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdhyanApp.user')),
            ],
        ),
    ]
