from rest_framework import serializers
from .models import world,countries,states

class WorldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= world
        fields=('total_cases','deaths','recovered','active')

class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=countries
        fields=('country','total_cases','deaths','recovered','active','new_cases','new_deaths')

class StatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        moddel=states
        fields=('state','total_cases','deaths','recovered')
