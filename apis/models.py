# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup,on_delete=models.CASCADE,)
    permission = models.ForeignKey('AuthPermission',on_delete=models.CASCADE,)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType',on_delete=models.CASCADE,)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE,)
    group = models.ForeignKey(AuthGroup,on_delete=models.CASCADE,)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE,)
    permission = models.ForeignKey(AuthPermission,on_delete=models.CASCADE,)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True,on_delete=models.CASCADE,)
    user = models.ForeignKey(AuthUser,on_delete=models.CASCADE,)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FollowList(models.Model):
    user_id = models.CharField(max_length=30)
    story_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'follow_list'


class Message(models.Model):
    message_content = models.CharField(max_length=30)
    commenter = models.CharField(max_length=30)
    message_created_dt = models.DateTimeField()
    like_counts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Story(models.Model):
    story_title = models.CharField(max_length=30)
    story_author = models.CharField(max_length=30)
    story_first_sentence = models.CharField(max_length=30)
    story_created_dt = models.DateTimeField()
    message_counts = models.IntegerField(blank=True, null=True)
    follow_counts = models.IntegerField(blank=True, null=True)
    story_theme = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'story'


class Theme(models.Model):
    theme_id = models.CharField(primary_key=True, max_length=11)

    class Meta:
        managed = False
        db_table = 'theme'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30)
    user_password = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_picture = models.CharField(max_length=70)
    user_mail = models.CharField(max_length=70)
    user_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'
