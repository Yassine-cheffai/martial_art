# Generated by Django 2.1.2 on 2020-08-04 23:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('phone', models.CharField(max_length=20, verbose_name='phone number')),
                ('address', models.CharField(max_length=254, verbose_name='address')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ['-date_joined'],
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUserProfile',
            fields=[
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='last modified')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='age')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d', verbose_name='photo')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='gender')),
            ],
        ),
        migrations.CreateModel(
            name='PrivacySettings',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('real_name_p', models.CharField(choices=[('pb', 'Public'), ('fr', 'Friends'), ('jm', 'Just me')], default='pb', max_length=2, verbose_name='real name privacy')),
                ('email_p', models.CharField(choices=[('pb', 'Public'), ('fr', 'Friends'), ('jm', 'Just me')], default='pb', max_length=2, verbose_name='email privacy')),
                ('phone_p', models.CharField(choices=[('pb', 'Public'), ('fr', 'Friends'), ('jm', 'Just me')], default='pb', max_length=2, verbose_name='phone privacy')),
                ('address_p', models.CharField(choices=[('pb', 'Public'), ('fr', 'Friends'), ('jm', 'Just me')], default='pb', max_length=2, verbose_name='address privacy')),
                ('profile_p', models.CharField(choices=[('pb', 'Public'), ('fr', 'Friends'), ('jm', 'Just me')], default='pb', max_length=2, verbose_name='profile privacy')),
                ('friend_list_p', models.CharField(choices=[('pb', 'Public'), ('fr', 'Friends'), ('jm', 'Just me')], default='pb', max_length=2, verbose_name='friends privacy')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]