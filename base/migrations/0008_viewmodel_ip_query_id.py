# Generated by Django 4.2.4 on 2023-09-02 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_adminloginpage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewmodel',
            name='ip_query_id',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
