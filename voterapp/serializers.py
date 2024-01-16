from rest_framework import serializers
from .models import Voter, PollingCenter

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'

class PollingCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollingCenter
        fields = '__all__'