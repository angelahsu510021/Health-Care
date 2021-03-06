# Generated by Django 3.1.7 on 2021-05-18 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
