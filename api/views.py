from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ElectricitySerializer
from users.models import WimhElectricity

# All urls need admin authentication

# setData to add data
@api_view(['POST'])
@permission_classes([IsAdminUser, IsAuthenticated])
def setData(request):
    serializer = ElectricitySerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# getData to get data
@api_view(['GET'])
@permission_classes([IsAdminUser, IsAuthenticated])
def getData(request, pk):
    object = WimhElectricity.objects.get(id=pk)
    serializer = ElectricitySerializer(object, many=False)
    return Response(serializer.data)