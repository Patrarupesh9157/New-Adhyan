# Generated by Django 4.0.3 on 2022-04-09 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0027_review_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='course',
        ),
    ]
