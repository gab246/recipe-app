from django.db import models

class Recipes(models.Model):
  name = models.CharField(max_length = 80)
  ingredients = models.TextField()
  cooking_time = models.IntegerField()

# Create your models here.

  def __str__(self):
    return str(self.name)
