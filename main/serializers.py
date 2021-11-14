from rest_framework import serializers

from .models import Stat


class GetStatSerializer(serializers.ModelSerializer):
    start = serializers.DateField()
    end = serializers.DateField()

    class Meta:
        model = Stat
        fields = ('start', 'end',)


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = ('date', "views", "clicks", "cost",)
