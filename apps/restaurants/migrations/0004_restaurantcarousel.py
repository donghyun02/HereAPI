# Generated by Django 3.2.7 on 2021-11-01 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_seat_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='restaurant_carousel', verbose_name='사진')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='restaurants.restaurant', verbose_name='식당')),
            ],
            options={
                'verbose_name': '캐러셀 이미지',
                'verbose_name_plural': '캐러셀 이미지',
            },
        ),
    ]
