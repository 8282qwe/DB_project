# Generated by Django 3.2.9 on 2021-11-28 01:38

import Movie.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discountrate',
            fields=[
                ('등급', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('할인율', models.IntegerField()),
            ],
            options={
                'db_table': 'discountrate',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('영화번호', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('영화제목', models.CharField(max_length=30)),
                ('영화감독', models.CharField(max_length=20)),
                ('주연배우', models.CharField(max_length=20)),
                ('포스터', models.ImageField(blank=True, null=True, upload_to='')),
                ('줄거리', models.TextField(blank=True, null=True)),
                ('평점', models.FloatField(default=5)),
            ],
            options={
                'db_table': 'movies',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('상영관번호', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('상영관형태', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'theater',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Theaterseat',
            fields=[
                ('상영관번호', models.OneToOneField(db_column='상영관번호', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Movie.theater')),
                ('행번호', models.CharField(max_length=5)),
                ('총좌석수', models.IntegerField()),
                ('위치번호', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'theaterseat',
                'managed': True,
                'unique_together': {('상영관번호', '행번호', '위치번호')},
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('회원이름', models.CharField(max_length=20)),
                ('휴대전화', models.CharField(max_length=15)),
                ('카드번호', models.CharField(max_length=26)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('등급', models.ForeignKey(db_column='등급', on_delete=django.db.models.deletion.DO_NOTHING, to='Movie.discountrate')),
            ],
            options={
                'db_table': 'people',
                'managed': True,
            },
            managers=[
                ('objects', Movie.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Movieschedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('상영시간', models.DateTimeField(default=django.utils.timezone.now)),
                ('요금', models.CharField(max_length=10)),
                ('상영관번호', models.ForeignKey(db_column='상영관번호', on_delete=django.db.models.deletion.DO_NOTHING, to='Movie.theater')),
                ('영화번호', models.ForeignKey(db_column='영화제목', on_delete=django.db.models.deletion.DO_NOTHING, to='Movie.movies')),
            ],
            options={
                'db_table': 'movieschedule',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('평점', models.IntegerField()),
                ('후기', models.CharField(max_length=200)),
                ('작성일자', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('영화', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Movie.movies')),
                ('작성자', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'board',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ticketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('예매일시', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('예매좌석', models.CharField(max_length=20)),
                ('금액', models.CharField(max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('영화번호', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='Movie.movieschedule')),
                ('상영관번호', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Movie.theaterseat')),
            ],
            options={
                'db_table': 'ticketing',
                'managed': True,
            },
        ),
        migrations.AddConstraint(
            model_name='movieschedule',
            constraint=models.UniqueConstraint(fields=('상영시간', '상영관번호'), name='unique reservations'),
        ),
        migrations.AlterUniqueTogether(
            name='ticketing',
            unique_together={('영화번호', '상영관번호', '예매일시')},
        ),
    ]