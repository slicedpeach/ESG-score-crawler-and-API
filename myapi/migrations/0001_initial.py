# Generated by Django 4.0.5 on 2022-06-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rank', models.IntegerField(max_length=10000)),
                ('total_industries', models.IntegerField(max_length=10000)),
                ('esgscore', models.IntegerField(max_length=100)),
                ('environmental', models.IntegerField(max_length=100)),
                ('social', models.IntegerField(max_length=100)),
                ('governance', models.IntegerField(max_length=100)),
            ],
        ),
    ]
