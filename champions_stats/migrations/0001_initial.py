# Generated by Django 5.1.4 on 2024-12-14 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Players",
            fields=[
                ("id_player", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "player_name",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "nationality",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "field_position",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("position", models.CharField(blank=True, max_length=100, null=True)),
                ("weight", models.FloatField(blank=True, null=True)),
                ("height", models.FloatField(blank=True, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                (
                    "player_image",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "db_table": "Players",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Teams",
            fields=[
                ("team_id", models.IntegerField(primary_key=True, serialize=False)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("team", models.CharField(blank=True, max_length=100, null=True)),
                ("logo", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "Teams",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Attacking",
            fields=[
                (
                    "id_player",
                    models.OneToOneField(
                        db_column="id_player",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="champions_stats.players",
                    ),
                ),
                ("assists", models.IntegerField(blank=True, null=True)),
                ("corners_taken", models.IntegerField(blank=True, null=True)),
                ("offsides", models.IntegerField(blank=True, null=True)),
                ("dribbles", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "Attacking",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Attempts",
            fields=[
                (
                    "id_player",
                    models.OneToOneField(
                        db_column="id_player",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="champions_stats.players",
                    ),
                ),
                ("total_attempts", models.IntegerField(blank=True, null=True)),
                ("attempts_on_target", models.IntegerField(blank=True, null=True)),
                ("attempts_off_target", models.IntegerField(blank=True, null=True)),
                ("blocked", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "Attempts",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Defending",
            fields=[
                (
                    "id_player",
                    models.OneToOneField(
                        db_column="id_player",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="champions_stats.players",
                    ),
                ),
                ("balls_recovered", models.IntegerField(blank=True, null=True)),
                ("tackles", models.IntegerField(blank=True, null=True)),
                ("tackles_won", models.IntegerField(blank=True, null=True)),
                ("tackles_lost", models.IntegerField(blank=True, null=True)),
                ("clearance_attempted", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "Defending",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Disciplinary",
            fields=[
                (
                    "id_player",
                    models.OneToOneField(
                        db_column="id_player",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="champions_stats.players",
                    ),
                ),
                ("fouls_committed", models.IntegerField(blank=True, null=True)),
                ("fouls_suffered", models.IntegerField(blank=True, null=True)),
                ("yellow_cards", models.IntegerField(blank=True, null=True)),
                ("red_cards", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "Disciplinary",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Distribution",
            fields=[
                (
                    "id_player",
                    models.OneToOneField(
                        db_column="id_player",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="champions_stats.players",
                    ),
                ),
                ("passing_accuracy", models.FloatField(blank=True, null=True)),
                ("passes_attempted", models.IntegerField(blank=True, null=True)),
                ("passes_completed", models.IntegerField(blank=True, null=True)),
                ("crossing_accuracy", models.FloatField(blank=True, null=True)),
                ("crosses_attempted", models.IntegerField(blank=True, null=True)),
                ("crosses_completed", models.IntegerField(blank=True, null=True)),
                ("free_kick_taken", models.IntegerField(blank=True, null=True)),
                ("matches_appearance", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "Distribution",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Goalkeeping",
            fields=[
                (
                    "id_player",
                    models.OneToOneField(
                        db_column="id_player",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="champions_stats.players",
                    ),
                ),
                ("saves", models.IntegerField(blank=True, null=True)),
                ("goals_conceded", models.IntegerField(blank=True, null=True)),
                ("saves_on_penalty", models.IntegerField(blank=True, null=True)),
                ("clean_sheets", models.IntegerField(blank=True, null=True)),
                ("punches_made", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "Goalkeeping",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Goals",
            fields=[
                (
                    "id_player",
                    models.OneToOneField(
                        db_column="id_player",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="champions_stats.players",
                    ),
                ),
                ("goals", models.IntegerField(blank=True, null=True)),
                ("inside_area", models.IntegerField(blank=True, null=True)),
                ("outside_area", models.IntegerField(blank=True, null=True)),
                ("right_foot", models.IntegerField(blank=True, null=True)),
                ("left_foot", models.IntegerField(blank=True, null=True)),
                ("head", models.IntegerField(blank=True, null=True)),
                ("other", models.IntegerField(blank=True, null=True)),
                ("penalties_scored", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "Goals",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Keystats",
            fields=[
                (
                    "id_player",
                    models.OneToOneField(
                        db_column="id_player",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="champions_stats.players",
                    ),
                ),
                ("distance_covered", models.FloatField(blank=True, null=True)),
                ("top_speed", models.FloatField(blank=True, null=True)),
                ("minutes_played", models.IntegerField(blank=True, null=True)),
                ("matches_appearance", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "KeyStats",
                "managed": False,
            },
        ),
    ]
