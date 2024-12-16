# flake8: noqa
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attacking(models.Model):
    id_player = models.OneToOneField('Players', models.DO_NOTHING, db_column='id_player', primary_key=True)
    assists = models.IntegerField(blank=True, null=True)
    corners_taken = models.IntegerField(blank=True, null=True)
    offsides = models.IntegerField(blank=True, null=True)
    dribbles = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Attacking'


class Attempts(models.Model):
    id_player = models.OneToOneField('Players', models.DO_NOTHING, db_column='id_player', primary_key=True)
    total_attempts = models.IntegerField(blank=True, null=True)
    attempts_on_target = models.IntegerField(blank=True, null=True)
    attempts_off_target = models.IntegerField(blank=True, null=True)
    blocked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Attempts'


class Defending(models.Model):
    id_player = models.OneToOneField('Players', models.DO_NOTHING, db_column='id_player', primary_key=True)
    balls_recovered = models.IntegerField(blank=True, null=True)
    tackles = models.IntegerField(blank=True, null=True)
    tackles_won = models.IntegerField(blank=True, null=True)
    tackles_lost = models.IntegerField(blank=True, null=True)
    clearance_attempted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Defending'


class Disciplinary(models.Model):
    id_player = models.OneToOneField('Players', models.DO_NOTHING, db_column='id_player', primary_key=True)
    fouls_committed = models.IntegerField(blank=True, null=True)
    fouls_suffered = models.IntegerField(blank=True, null=True)
    yellow_cards = models.IntegerField(blank=True, null=True)
    red_cards = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Disciplinary'


class Distribution(models.Model):
    id_player = models.OneToOneField('Players', models.DO_NOTHING, db_column='id_player', primary_key=True)
    passing_accuracy = models.FloatField(blank=True, null=True)
    passes_attempted = models.IntegerField(blank=True, null=True)
    passes_completed = models.IntegerField(blank=True, null=True)
    crossing_accuracy = models.FloatField(blank=True, null=True)
    crosses_attempted = models.IntegerField(blank=True, null=True)
    crosses_completed = models.IntegerField(blank=True, null=True)
    free_kick_taken = models.IntegerField(blank=True, null=True)
    matches_appearance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Distribution'


class Goalkeeping(models.Model):
    id_player = models.OneToOneField('Players', models.DO_NOTHING, db_column='id_player', primary_key=True)
    saves = models.IntegerField(blank=True, null=True)
    goals_conceded = models.IntegerField(blank=True, null=True)
    saves_on_penalty = models.IntegerField(blank=True, null=True)
    clean_sheets = models.IntegerField(blank=True, null=True)
    punches_made = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Goalkeeping'


class Goals(models.Model):
    id_player = models.OneToOneField('Players', models.DO_NOTHING, db_column='id_player', primary_key=True)
    goals = models.IntegerField(blank=True, null=True)
    inside_area = models.IntegerField(blank=True, null=True)
    outside_area = models.IntegerField(blank=True, null=True)
    right_foot = models.IntegerField(blank=True, null=True)
    left_foot = models.IntegerField(blank=True, null=True)
    head = models.IntegerField(blank=True, null=True)
    other = models.IntegerField(blank=True, null=True)
    penalties_scored = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Goals'


class Keystats(models.Model):
    id_player = models.OneToOneField('Players', models.DO_NOTHING, db_column='id_player', primary_key=True)
    distance_covered = models.FloatField(blank=True, null=True)
    top_speed = models.FloatField(blank=True, null=True)
    minutes_played = models.IntegerField(blank=True, null=True)
    matches_appearance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'KeyStats'


class Players(models.Model):
    id_player = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=100, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    field_position = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    id_team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='id_team', blank=True, null=True)
    player_image = models.CharField(max_length=255, blank=True, null=True)

    @property
    def team_name(self):
        return self.id_team.team if self.id_team else None

    class Meta:
        managed = False
        db_table = 'Players'


class Teams(models.Model):
    team_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Teams'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
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
