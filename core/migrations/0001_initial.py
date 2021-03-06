# Generated by Django 2.2.10 on 2020-03-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification', models.CharField(max_length=100, verbose_name='identification')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
                ('tema', models.CharField(max_length=100, verbose_name='Tema')),
                ('url', models.CharField(max_length=100, verbose_name='URL')),
                ('likes', models.IntegerField(verbose_name='Likes')),
                ('deslikes', models.IntegerField(verbose_name='Deslikes')),
                ('score', models.IntegerField(verbose_name='score')),
            ],
        ),
    ]
