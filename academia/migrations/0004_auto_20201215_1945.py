# Generated by Django 3.1.3 on 2020-12-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0003_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceAlg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAlg_Graphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceDs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceGraphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500, verbose_name='link')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceTh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=500, verbose_name='link')),
            ],
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
