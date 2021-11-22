from decimal import Decimal

from django.db import models

from apps.restaurants.managers import ReviewManager


class Restaurant(models.Model):
    name = models.CharField(
        verbose_name='이름',
        max_length=255,
    )
    image = models.ImageField(
        verbose_name='사진',
        upload_to='restaurants',
        null=True
    )
    address = models.TextField(
        verbose_name='주소',
    )
    types = models.ManyToManyField(
        'Type',
        verbose_name='식당 종류',
    )

    class Meta:
        verbose_name = '식당'
        verbose_name_plural = '식당'

    def __str__(self):
        return f'[식당 {self.id}] 이름: {self.name}'

    def get_rating(self) -> Decimal:
        return self.reviews.get_rating()


class Type(models.Model):
    name = models.CharField(
        verbose_name='이름',
        max_length=20,
    )
    code = models.CharField(
        verbose_name='코드',
        max_length=20,
    )

    class Meta:
        verbose_name = '식당 종류'
        verbose_name_plural = '식당 종류'

    def __str__(self):
        return f'[식당 종류 {self.id}] 이름: {self.name}'


class RestaurantCarousel(models.Model):
    restaurant = models.ForeignKey(
        'Restaurant',
        verbose_name='식당',
        related_name='carousel',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name='사진',
        upload_to='restaurant_carousel',
    )

    class Meta:
        verbose_name = '캐러셀 이미지'
        verbose_name_plural = '캐러셀 이미지'

    def __str__(self):
        return f'[캐러셀 이미지 {self.id}] 식당: {self.restaurant.name}'


class Review(models.Model):
    restaurant = models.ForeignKey(
        'restaurants.Restaurant',
        verbose_name='식당',
        related_name='reviews',
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        verbose_name='내용',
    )
    rating = models.DecimalField(
        verbose_name='평점',
        max_digits=3,
        decimal_places=2,
    )

    objects = ReviewManager()

    class Meta:
        verbose_name = '후기'
        verbose_name_plural = '후기'

    def __str__(self):
        return f'[후기 {self.id}]'


class Seat(models.Model):
    restaurant = models.ForeignKey(
        'Restaurant',
        verbose_name='식당',
        related_name='seats',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        verbose_name='사진',
        upload_to='seats',
    )
    name = models.CharField(
        verbose_name='좌석명',
        max_length=128,
    )
    description = models.TextField(
        verbose_name='설명',
        blank=True,
    )

    class Meta:
        verbose_name = '좌석'
        verbose_name_plural = '좌석'

    def __str__(self):
        return f'[좌석 {self.id}] 식당: {self.restaurant.name}'


class Reservation(models.Model):
    seat = models.ForeignKey(
        'Seat',
        verbose_name='좌석',
        on_delete=models.CASCADE,
        related_name='reservations',
    )
    reserved_datetime = models.DateTimeField(
        '예약시간',
    )
    booker_name = models.CharField(
        '예약자 이름',
        max_length=20,
    )
    booker_email = models.EmailField(
        '예약자 이메일',
    )
    booker_phone_number = models.CharField(
        '예약자 전화번호',
        max_length=20,
    )

    class Meta:
        verbose_name = '예약'
        verbose_name_plural = '예약'

    def __str__(self):
        return (
            f'[예약 {self.id}] '
            f'예약자: {self.booker_name}, '
            f'예약시간: {self.reserved_datetime.strftime("YYYY-MM-DD HH:mm")}'
        )
