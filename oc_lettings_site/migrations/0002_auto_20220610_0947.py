# Generated by Django 3.0 on 2022-06-10 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.DeleteModel(
                    name='profile',
                ),
            ],
            database_operations=[
                migrations.AlterModelTable(
                    name='profile',
                    table='profiles_profile',
                ),
            ],
        )
        
    ]
