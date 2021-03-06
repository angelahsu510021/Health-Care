# Generated by Django 3.1.7 on 2021-06-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitforum', '0006_auto_20210610_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='del_pass',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='nickname',
            field=models.CharField(default='People who are unwilling to reveal their identity', max_length=100),
        ),
    ]
