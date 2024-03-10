from .models import Pizza
from rest_framework import viewsets, permissions
from .serializers import PizzasSerializer

class PizzasViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class= PizzasSerializer