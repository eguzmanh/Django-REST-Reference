from rest_framework import serializers
from .models import Drink

# Class to serialize Drink object data and fixing the format
# of the response message to match id, name, description
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink # model used for the Serializer
        fields = ['id', 'name', 'description'] # serializer format