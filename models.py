from django.db import models
from django.conf import settings
# Create your models here.
class Users(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)
    user_name = models.CharField(max_length=256)
    booked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user_name}"
class MeetingBookModel(models.Model):
    user_name=models.ForeignKey(Users,on_delete=models.CASCADE,null=True)
    date=models.DateField()
    time=models.TimeField()
    booked = models.BooleanField(default=False)
    # location=models.CharField(max_length=255)
    TableA = 'TableA'
    TableB = 'TableB'
    TableC = 'TableC'
    TableD = 'TableD'
    TableE = 'TableE'
    location_choices = [
        (TableA, 'TableA'),
        (TableB, 'TableB'),
        (TableC, 'TableC'),
        (TableD, 'TableD'),
        (TableE, 'TableE'),
    ]
    location = models.CharField(
        max_length=200,
        choices=location_choices,
        default=TableA,
    )