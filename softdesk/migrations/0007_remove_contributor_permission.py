# Generated by Django 4.1.3 on 2022-12-19 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk', '0006_rename_author_user_id_comment_author_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contributor',
            name='permission',
        ),
    ]
