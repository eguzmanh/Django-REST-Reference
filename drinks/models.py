from django.db import models

# Drinks stored in the database have a name and a description
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    # When outputting a Drink object, it will display the name attribute
    def __str__(self):
        return self.name
