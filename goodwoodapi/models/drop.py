from django.db import models
from django.contrib.auth.models import User


class Drop(models.Model):

    arborist = models.ForeignKey("GoodWoodUser", on_delete=models.CASCADE)
    woodworker = models.ForeignKey("Category", on_delete=models.CASCADE)
    wood_type = models.CharField(max_length=50)
    cut_date = models.DateField()
    availability = models.BooleanField()
