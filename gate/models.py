from django.db import models

# Create your models here.
from django.db import models

class GateLog(models.Model):
    visitor_name = models.CharField(max_length=100)
    visitor_type = models.CharField(max_length=20)
    visit_time = models.IntegerField()
    frequency_7d = models.IntegerField()
    intent = models.CharField(max_length=20)
    approval_probability = models.FloatField()
    anomaly_score = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
