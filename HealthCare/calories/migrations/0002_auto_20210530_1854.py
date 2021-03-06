from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfood',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='postfood',
            name='calorie_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]
