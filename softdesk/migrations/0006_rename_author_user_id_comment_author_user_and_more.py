# Generated by Django 4.1.3 on 2022-12-19 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0005_contributor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_user_id',
            new_name='author_user',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='issue_id',
            new_name='issue',
        ),
        migrations.RenameField(
            model_name='contributor',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='contributor',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='assignee_user_id',
            new_name='assignee_user',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='author_user_id',
            new_name='author_user',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='author_user_id',
            new_name='author_user',
        ),
    ]
