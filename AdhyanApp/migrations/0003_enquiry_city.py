# Generated by Django 4.0.2 on 2022-03-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdhyanApp', '0002_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='city',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
