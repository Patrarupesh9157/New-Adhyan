# Generated by Django 4.0.3 on 2022-04-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0028_remove_review_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_course',
            name='codiscription',
            field=models.TextField(max_length=1000),
        ),
    ]