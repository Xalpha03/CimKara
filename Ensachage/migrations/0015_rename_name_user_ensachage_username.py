# Generated by Django 5.0.1 on 2024-02-04 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ensachage', '0014_alter_ensachage_vrac'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ensachage',
            old_name='name_user',
            new_name='username',
        ),
    ]
