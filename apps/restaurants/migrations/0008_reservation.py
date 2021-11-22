# Generated by Django 3.2.7 on 2021-11-22 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_alter_type_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved_datetime', models.DateTimeField(verbose_name='예약시간')),
                ('booker_name', models.CharField(max_length=20, verbose_name='예약자 이름')),
                ('booker_email', models.EmailField(max_length=254, verbose_name='예약자 이메일')),
                ('booker_phone_number', models.CharField(max_length=20, verbose_name='예약자 전화번호')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='restaurants.seat', verbose_name='좌석')),
            ],
            options={
                'verbose_name': '예약',
                'verbose_name_plural': '예약',
            },
        ),
    ]
