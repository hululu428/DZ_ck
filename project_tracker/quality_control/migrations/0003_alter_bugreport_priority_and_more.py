# Generated by Django 5.0.4 on 2024-04-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0002_alter_featurerequest_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='priority',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=1),
        ),
        migrations.AlterField(
            model_name='featurerequest',
            name='priority',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=1),
        ),
    ]