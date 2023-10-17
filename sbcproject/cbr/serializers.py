from rest_framework import serializers
from .models import SBCReport

class SBCReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SBCReport
        fields = '__all__'