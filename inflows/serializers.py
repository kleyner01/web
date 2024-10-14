from rest_framework import serializers
from inflows.models import Inflow


class InflowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inflow
        fileds = '__all__'
