# Generated by Django 4.2.4 on 2023-08-19 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Roadmap', '0002_roadmapmodel_md'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='road_map_handle',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Roadmap.roadmapmodel', verbose_name='main_page_roadmap'),
        ),
    ]
