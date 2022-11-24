from django.db import models
from django.conf import settings
from datetime import date

Slots = (
        ('9.00 - 10.00', '9.00 - 10.00'),
        ('10.00 - 11.00', '10.00 - 11.00'),
        ('11.00 - 12.00', '11.00 - 12.00'),
        ('12.00 - 13.00', '12.00 - 13.00'),
        ('13.00 - 14.00', '13.00 - 14.00'),
        ('14.00 - 15.00', '14.00 - 15.00'),
        ('15.00 - 16.00', '15.00 - 16.00'),
        ('16.00 - 17.00', '16.00 - 17.00'),
        ('17.00 - 18.00', '17.00 - 18.00'),
)


class Booking(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    slot = models.CharField(max_length=15, choices=Slots)
    booking_date = models.CharField(max_length=15, default='foo')

    def __str__(self):
        return f'{self.user} has booked a PT at {self.slot} on {self.booking_date}'
