# Generated by Django 4.1.1 on 2022-10-16 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postit', '0004_postit_timestamp_postlike_postit_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='postit',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='postit.postit'),
        ),
    ]