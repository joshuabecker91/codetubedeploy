# Generated by Django 4.1.1 on 2022-09-19 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codetubeApp', '0002_rename_createdat_user_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liked',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='liked',
            old_name='video_id',
            new_name='video',
        ),
        migrations.RemoveField(
            model_name='liked',
            name='like_id',
        ),
    ]
