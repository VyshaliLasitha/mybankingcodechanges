# Generated by Django 4.0.5 on 2022-06-10 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerFeedback', '0003_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='CustomerFeedback',
        ),
    ]