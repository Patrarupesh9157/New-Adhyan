# Generated by Django 4.0.3 on 2022-04-09 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0026_review_alter_register_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Myapp.all_course'),
        ),
    ]
