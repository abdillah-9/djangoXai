# Generated by Django 5.0.4 on 2024-07-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_assets_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assets',
            name='pimage',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assets',
            name='pname',
            field=models.CharField(max_length=100),
        ),
    ]
