from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

