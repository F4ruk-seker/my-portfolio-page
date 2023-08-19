# Generated by Django 4.2.4 on 2023-08-19 05:16

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Roadmap', '0002_roadmapmodel_md'),
        ('projects', '0006_alter_technologies_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.TextField()),
                ('is_i_am', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keywords', models.TextField(null=True)),
                ('robots', models.TextField(null=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image_alt', models.TextField(null=True)),
                ('view', models.ManyToManyField(blank=True, default=None, editable=False, to='base.viewmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keywords', models.TextField(null=True)),
                ('robots', models.TextField(null=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image_alt', models.TextField(null=True)),
                ('road_map_handle', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Roadmap.roadmapmodel', verbose_name='main_page_roadmap')),
                ('top_3_projects', models.ManyToManyField(blank=True, to='projects.projects')),
                ('view', models.ManyToManyField(blank=True, default=None, editable=False, to='base.viewmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CvPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keywords', models.TextField(null=True)),
                ('robots', models.TextField(null=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image_alt', models.TextField(null=True)),
                ('view', models.ManyToManyField(blank=True, default=None, editable=False, to='base.viewmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('keywords', models.TextField(null=True)),
                ('robots', models.TextField(null=True)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('image_alt', models.TextField(null=True)),
                ('view', models.ManyToManyField(blank=True, default=None, editable=False, to='base.viewmodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
