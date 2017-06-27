# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-27 15:32
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import ordd_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso2', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_reviewed', models.BooleanField(default=False)),
                ('review_date', models.DateTimeField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('notes', models.CharField(blank=True, max_length=4096)),
                ('is_digital_form', models.BooleanField()),
                ('is_pub_available', models.BooleanField()),
                ('is_avail_for_free', models.BooleanField()),
                ('is_machine_read', models.BooleanField()),
                ('is_bulk_avail', models.BooleanField()),
                ('is_open_licence', models.BooleanField()),
                ('is_prov_timely', models.BooleanField()),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordd_api.Country')),
            ],
        ),
        migrations.CreateModel(
            name='KeyDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('format', models.CharField(max_length=32)),
                ('comment', models.CharField(max_length=1024)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LevDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LevDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LevScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OptIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=ordd_api.models.my_random_key, max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Peril',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256)),
                ('institution', models.CharField(blank=True, max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=4096)),
            ],
        ),
        migrations.AddField(
            model_name='keydataset',
            name='applicability',
            field=models.ManyToManyField(to='ordd_api.Peril'),
        ),
        migrations.AddField(
            model_name='keydataset',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordd_api.Category'),
        ),
        migrations.AddField(
            model_name='keydataset',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordd_api.LevDataset'),
        ),
        migrations.AddField(
            model_name='keydataset',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordd_api.LevDescription'),
        ),
        migrations.AddField(
            model_name='keydataset',
            name='scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordd_api.LevScale'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='keydataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_dataset', to='ordd_api.KeyDataset'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datasets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dataset',
            name='url',
            field=models.ManyToManyField(to='ordd_api.Url'),
        ),
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordd_api.Region'),
        ),
        migrations.AlterUniqueTogether(
            name='keydataset',
            unique_together=set([('category', 'code'), ('category', 'dataset', 'description', 'scale')]),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='tag',
            field=models.ManyToManyField(to='ordd_api.Tag'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='tag',
            field=models.ManyToManyField(blank=True, to='ordd_api.Tag'),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='url',
            field=models.ManyToManyField(blank=True, to='ordd_api.Url'),
        ),
    ]
