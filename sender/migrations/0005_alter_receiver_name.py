# Generated by Django 5.0.3 on 2024-03-13 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0004_remove_receiver_timestemp_receiver_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiver',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
