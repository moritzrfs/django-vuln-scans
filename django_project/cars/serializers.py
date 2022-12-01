# import rest framework modules
from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

        extra_kwargs = {
            'creator': {'read_only': True}
        }

    # add additional serializer for creation fo a car

class CreateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        # make engine optional
        extra_kwargs = {"engine": {"required": False}}
        
    # make validation for seats
    def validate_seats(self, value):
        if value <= 1:
            raise serializers.ValidationError("Seats must be greater than 2")
        return value
