from django.db import models
from django.db.models import Avg


class ReviewManager(models.Manager):
    def get_rating(self):
        return self.aggregate(
            rating_average=Avg('rating'),
        )['rating_average']


class ReservationManager(models.Manager):
    def get_reserved_times(self, seat_id, date):
        return self.filter(
            seat_id=seat_id,
            reserved_datetime__date=date,
        ).values_list(
            'reserved_datetime__time',
            flat=True,
        )
