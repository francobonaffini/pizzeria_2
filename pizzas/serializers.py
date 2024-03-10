from rest_framework import serializers
from .models import Pizza

class PizzasSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Pizza
        fields = ('id','name','desciption','price','image')
        
