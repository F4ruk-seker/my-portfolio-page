# Generated by Django 4.2.4 on 2023-08-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_gamepage'),
        ('Game', '0003_rename_id_game_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='view',
            field=models.ManyToManyField(blank=True, default=None, editable=False, to='base.viewmodel'),
        ),
        migrations.AlterField(
            model_name='gamevideomodel',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='gamevideomodel',
            name='video_length',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]