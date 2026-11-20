from django.db import models

class FoodItem(models.Model):
    food_name = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.food_name