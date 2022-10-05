# Generated by Django 4.1.1 on 2022-10-04 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postit',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True, serialize=False,
                                           verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True,
                                           null=True, upload_to='images/')),
            ],
        ),
    ]
