from rest_framework import serializers
from .models import world

class WorldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= world
        fields=('country','total_cases','total_deaths','total_recovered','new_cases','new_deaths')