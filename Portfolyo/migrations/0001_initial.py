# Generated by Django 4.1.6 on 2023-02-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0004_remove_projects_image_projects_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('url', models.URLField()),
                ('profession', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('organisation', models.ManyToManyField(to='Portfolyo.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('certificate_id', models.TextField(default=None, null=True)),
                ('verification', models.TextField(null=True)),
                ('priority', models.IntegerField()),
                ('date', models.DateField(null=True)),
                ('organisation', models.ManyToManyField(to='Portfolyo.organisation')),
                ('technologies', models.ManyToManyField(to='projects.technologies')),
            ],
        ),
    ]
