from rest_framework.decorators import api_view
from rest_framework.response import Response

from rentals.models import Place
from rentals.serializers import PlaceSerializer

@api_view(['GET'])
def get_all_places(request):
    places = Place.objects.all()
    serializer = PlaceSerializer(places, many= True)
    return Response(serializer.data,status=200)

# Create your views here.
