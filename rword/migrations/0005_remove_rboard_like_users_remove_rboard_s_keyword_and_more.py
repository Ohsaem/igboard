# Generated by Django 4.1 on 2022-08-15 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rword', '0004_remove_rboard_word_tag_rboard_s_keyword_delete_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rboard',
            name='like_users',
        ),
        migrations.RemoveField(
            model_name='rboard',
            name='s_keyword',
        ),
        migrations.RemoveField(
            model_name='rboard',
            name='writer',
        ),
        migrations.DeleteModel(
            name='RBoardLikeUsers',
        ),
        migrations.DeleteModel(
            name='RBoard',
        ),
    ]
