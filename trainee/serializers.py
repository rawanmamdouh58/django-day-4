# trainee/serializers.py
from rest_framework import serializers
from trainee.models import Trainee

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'