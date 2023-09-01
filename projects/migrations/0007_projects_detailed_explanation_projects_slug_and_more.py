# Generated by Django 4.2.4 on 2023-08-22 04:43

import autoslug.fields
import cloudinary.models
from django.db import migrations, models
import django.utils.text
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_adminloginpage'),
        ('projects', '0006_alter_technologies_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='detailed_explanation',
            field=mdeditor.fields.MDTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default=django.utils.timezone.now, editable=False, populate_from='title', slugify=django.utils.text.slugify),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='view',
            field=models.ManyToManyField(to='base.viewmodel'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='thumbnail'),
        ),
    ]