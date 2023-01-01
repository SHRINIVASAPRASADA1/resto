# Generated by Django 4.1.3 on 2022-12-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_bestmenu_ratting_alter_bestmenu_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Description', models.TextField()),
                ('amount', models.IntegerField()),
                ('img', models.ImageField(upload_to='menu/')),
                ('Date', models.DateTimeField(auto_now=True)),
                ('subTitle', models.TextField(blank=True)),
                ('Ratting', models.IntegerField(null=True)),
            ],
        ),
    ]
