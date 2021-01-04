# Generated by Django 2.1.2 on 2020-08-04 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('content', models.CharField(max_length=140, verbose_name='comment')),
            ],
            options={
                'ordering': ['-created_time', '-last_modified'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('content', models.CharField(max_length=140, verbose_name='post')),
                ('privacy_level', models.CharField(choices=[('pb', 'Public'), ('fr', 'Friends'), ('jm', 'Just me')], default='pb', max_length=2, verbose_name='privacy level')),
            ],
            options={
                'ordering': ['-created_time', '-last_modified'],
            },
        ),
    ]
