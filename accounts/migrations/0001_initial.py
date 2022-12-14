# Generated by Django 4.1 on 2022-08-11 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=32, unique=True, verbose_name='유저 아이디')),
                ('user_pw', models.CharField(max_length=128, verbose_name='유저 비밀번호')),
            ],
            options={
                'verbose_name': '유저',
                'verbose_name_plural': '유저',
                'db_table': 'user',
            },
        ),
    ]
