# Generated by Django 4.1.3 on 2022-12-31 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_addtocart'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
