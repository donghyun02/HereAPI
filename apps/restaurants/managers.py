from django.db import models
from django.db.models import Avg


class ReviewManager(models.Manager):
    def get_rating(self):
        return self.aggregate(
            rating_average=Avg('rating'),
        )['rating_average']
