# Generated by Django 3.1.7 on 2021-04-07 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pu_date',
            new_name='pub_date',
        ),
    ]
