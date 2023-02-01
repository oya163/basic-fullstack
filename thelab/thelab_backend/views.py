"""Views module for CompanyName"""

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CompanyName
from .serializers import CompanyNameSerializer

class CompanyNameDetail(APIView):
    """REST API class for an CompanyName object"""

    def get(self, _):
        """
            Returns latest serialized CompanyName
            object based on updated_at date
        """
        name = CompanyName.objects.latest('updated_at')
        serializer = CompanyNameSerializer(name)
        return Response(serializer.data)
