# Generated by Django 4.1.1 on 2022-10-05 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postit',
            options={'ordering': ['-id']},
        ),
    ]
