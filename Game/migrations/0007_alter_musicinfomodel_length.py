# Generated by Django 4.2.4 on 2023-08-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0006_alter_musicinfomodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicinfomodel',
            name='length',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
