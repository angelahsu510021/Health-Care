# Generated by Django 3.2.3 on 2021-06-09 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitforum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('youtube_id', models.CharField(max_length=255)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitforum.level')),
            ],
        ),
    ]
