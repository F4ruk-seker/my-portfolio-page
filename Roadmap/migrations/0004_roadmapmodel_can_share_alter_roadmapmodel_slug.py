# Generated by Django 4.2.4 on 2023-08-20 07:34

import autoslug.fields
from django.db import migrations, models
import django.utils.text


class Migration(migrations.Migration):

    dependencies = [
        ('Roadmap', '0003_roadmapmodel_slug_alter_roadmapmodel_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadmapmodel',
            name='can_share',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='roadmapmodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='name', slugify=django.utils.text.slugify),
        ),
    ]
