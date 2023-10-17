from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SBCReport
from .serializers import SBCReportSerializer

class SBCReportView(APIView):
    def get(self, request, format=None):
        report = SBCReport.objects.all()
        serializer = SBCReportSerializer(report, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SBCReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

