# Generated by Django 4.2.7 on 2023-12-05 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_repository_link',
            new_name='repository_link',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='project_title',
            new_name='title',
        ),
    ]
