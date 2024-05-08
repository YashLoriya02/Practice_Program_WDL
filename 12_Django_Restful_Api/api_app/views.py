from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from rest_framework.response import Response
from .serializers import ItemSerializer

class Items(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def list(self, request):
        items = self.get_queryset()
        serializer = self.get_serializer(items, many=True)
        return render(request, 'item_list.html', {'items': serializer.data})

def home(request):
    return render(request, 'home.html')
