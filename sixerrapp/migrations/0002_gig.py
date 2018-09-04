# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-03 20:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sixerrapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('GD', 'Graphics & Design'), ('DM', 'Digital & Marketing'), ('VA', 'Video & Animation'), ('MA', 'Music & Audio'), ('PT', 'Programming & Tech')], max_length=2)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField(default=6)),
                ('photo', models.FileField(upload_to='gigs')),
                ('status', models.BooleanField(default=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
