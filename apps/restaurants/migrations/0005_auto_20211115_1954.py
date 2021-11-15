# Generated by Django 3.2.7 on 2021-11-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurantcarousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
            ],
            options={
                'verbose_name': '식당 종류',
                'verbose_name_plural': '식당 종류',
            },
        ),
        migrations.AddField(
            model_name='restaurant',
            name='types',
            field=models.ManyToManyField(to='restaurants.Type', verbose_name='식당 종류'),
        ),
    ]