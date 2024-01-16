from django.db import models

# Create your models here.
class Voter(models.Model):
    nid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class PollingCenter(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    center_name = models.CharField(max_length=100)
    slip_number = models.CharField(max_length=10)