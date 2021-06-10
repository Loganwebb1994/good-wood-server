from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related


class Drop(models.Model):

    arborist = models.ForeignKey("GoodWoodUser", on_delete=models.CASCADE, related_name="arborist")
    woodworker = models.ForeignKey("GoodWoodUser", on_delete=models.CASCADE, related_name="woodworker", null=True)
    wood_type = models.CharField(max_length=50)
    cut_date = models.DateField()
    availability = models.BooleanField()
