# Generated by Django 3.2.7 on 2021-10-07 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('address', models.TextField(verbose_name='주소')),
            ],
            options={
                'verbose_name': '식당',
                'verbose_name_plural': '식당',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='평점')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restaurants.restaurant', verbose_name='식당')),
            ],
            options={
                'verbose_name': '후기',
                'verbose_name_plural': '후기',
            },
        ),
    ]
