''' load models class'''
from django.db import models

GENDER_CHOICES = (
    ('default','همکار ارجمند'),
    ('sir', 'آقای'),
    ('madam','خانم'),
    )

# Create your models here.

class Book(models.Model):
    '''
    this is list of phone book
    '''

    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='default')
    name = models.CharField(max_length=50)
    organizationalUnit = models.CharField(max_length=50)
    floorUnit = models.CharField(max_length=50)
    organizationPhone = models.CharField(max_length=3)
    directPhone = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.name} {self.organizationalUnit}"
