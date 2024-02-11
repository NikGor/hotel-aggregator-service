from django.db import models


class MetaHotel(models.Model):
    id = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.id
