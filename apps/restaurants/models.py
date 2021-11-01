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

    class Meta:
        verbose_name = '식당'
        verbose_name_plural = '식당'

    def __str__(self):
        return f'[식당 {self.id}] 이름: {self.name}'

    def get_rating(self) -> Decimal:
        return self.reviews.get_rating()


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
        return f'[좌석 {self.id}] 식당: {self.restaurant_id}'
