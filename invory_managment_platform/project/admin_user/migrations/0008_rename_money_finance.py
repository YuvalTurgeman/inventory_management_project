# Generated by Django 4.1.3 on 2022-11-29 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0007_alter_money_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Money',
            new_name='Finance',
        ),
    ]
