from rest_framework import viewsets

from .serializers import HostelSerializer
from .models import Hostel
# Create your views here.


class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all().order_by('id')
    serializer_class = HostelSerializer
