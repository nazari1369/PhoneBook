from django.db import models

# Create your models here.
class Book(models.Model):
    GENDER_CHOICES = (('default','همکار ارجمند'),('sir', 'آقای'),('madam','خانم'))
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, default='default')
    name = models.CharField(max_length=50)
    organizationalUnit = models.CharField(max_length=50)
    floorUnit = models.CharField(max_length=50)
    organizationPhone = models.CharField(max_length=3)
    directPhone = models.CharField(max_length=8)