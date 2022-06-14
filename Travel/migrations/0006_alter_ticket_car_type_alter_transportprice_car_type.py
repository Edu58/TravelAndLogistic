# Generated by Django 4.0.5 on 2022-06-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0005_alter_transportprice_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='car_type',
            field=models.CharField(choices=[('Bus', '18 Seaters'), ('Mini Car', '4 Seaters'), ('Car', '6 Seaters')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='transportprice',
            name='car_type',
            field=models.CharField(choices=[('Bus', '18 Seaters'), ('Mini Car', '4 Seaters'), ('Car', '6 Seaters')], default=1, max_length=100),
        ),
    ]
