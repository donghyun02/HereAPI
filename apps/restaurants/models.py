from django.db import models


class Restaurant(models.Model):
    name = models.CharField(
        verbose_name='이름',
        max_length=255,
    )
    address = models.TextField(
        verbose_name='주소',
    )

    class Meta:
        verbose_name = '식당'
        verbose_name_plural = '식당'

    def __str__(self):
        return f'[식당 {self.id}] 이름: {self.name}'
