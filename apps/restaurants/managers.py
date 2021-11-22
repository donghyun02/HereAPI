from django.db import models
from django.db.models import Avg

from core.utils import send_email


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

    def reserve(self, seat_id, datetime, name, email, phone_number):
        obj = self._reserve(seat_id, datetime, name, email, phone_number)
        self._send_email(email, seat_id, datetime, name, phone_number)
        return obj

    def _reserve(self, seat_id, datetime, name, email, phone_number):
        return self.create(
            seat_id=seat_id,
            reserved_datetime=datetime,
            booker_name=name,
            booker_email=email,
            booker_phone_number=phone_number,
        )

    def _send_email(self, email, seat_id, datetime, name, phone_number):
        from apps.restaurants.models import Seat

        seat = Seat.objects.select_related('restaurant').get(id=seat_id)
        content = (
            f'예약이 다음과 같이 확정되었습니다.\n\n'
            f'식당명: {seat.restaurant.name}\n'
            f'좌석: {seat.name}\n'
            f'일시: {datetime.strftime("%Y-%m-%d %H:%M")}\n\n'
            f'예약자 성명: {name}\n'
            f'예약자 전화번호: {phone_number}'
        )
        send_email('[여기로] 예약 확정 안내', content, email)
