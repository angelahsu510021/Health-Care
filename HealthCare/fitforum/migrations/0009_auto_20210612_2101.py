# Generated by Django 3.2.3 on 2021-06-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitforum', '0008_auto_20210611_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
