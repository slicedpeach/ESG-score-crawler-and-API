# Generated by Django 4.0.5 on 2022-06-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_remove_company_total_industries'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='rank',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='ric',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]