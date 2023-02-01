"""Serializer module for CompanyName"""

from rest_framework import serializers

from .models import CompanyName


class CompanyNameSerializer(serializers.ModelSerializer):
    """
        Serializer for Company Name
    """
    class Meta:
        """
            Meta Class
        """
        model = CompanyName
        fields = '__all__'