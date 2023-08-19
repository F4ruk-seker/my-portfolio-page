# Generated by Django 4.2.4 on 2023-08-19 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameTypeModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(default=None, null=True)),
                ('icon', models.TextField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameVideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default=None, null=True)),
                ('description', models.TimeField()),
                ('video_length', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MusicInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default=None, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('image', models.TextField(default=None, null=True)),
                ('length', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GameInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=None, null=True)),
                ('game_type', models.ManyToManyField(to='Game.gametypemodels')),
            ],
        ),
    ]
