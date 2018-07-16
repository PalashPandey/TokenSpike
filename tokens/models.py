from django.db import models

# Create your models here.
class Cars(models.Model):
    ("HONDA", "HONDA"),
    ("FERRARI", "FERRARI" )

    car_make = models.CharField(max_length = 20 , choices= TYPE_CHOICES, default="HONDA")
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.car_make