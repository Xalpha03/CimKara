# Generated by Django 5.0.1 on 2024-02-03 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ensachage', '0007_alter_ensachage_vrac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ensachage',
            name='vrac',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
