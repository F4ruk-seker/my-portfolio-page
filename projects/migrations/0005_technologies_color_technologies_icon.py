# Generated by Django 4.1.6 on 2023-02-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_projects_image_projects_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologies',
            name='color',
            field=models.CharField(choices=[(' ', 'None'), ('text-primary', 'primary'), ('text-secondary', 'secondary'), ('text-success', 'success'), ('text-danger', 'danger'), ('text-warning', 'warning'), ('text-info', 'info'), ('text-light', 'light'), ('text-dark', 'dark'), ('text-muted', 'muted'), ('text-white', 'white'), ('link-primary', 'l-primary'), ('link-secondary', 'l-secondary'), ('link-success', 'l-success'), ('link-danger', 'l-danger'), ('link-warning', 'l-warning'), ('link-info', 'l-info'), ('link-light', 'l-light'), ('link-dark', 'l-dark'), ('link-muted', 'l-muted'), ('link-white', 'l-white')], default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='technologies',
            name='icon',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
