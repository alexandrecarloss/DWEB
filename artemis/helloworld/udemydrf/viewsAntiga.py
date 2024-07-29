from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from adocao.models import Produto
from .serializers import ProdutoSerializer

class ProdutoAPIView(APIView):
    """
        API de produtos
    """
    def get(self, request):
        print(request.data)
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
        

    def post(selt, request):
        serializer = ProdutoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
def prod(request):
    response = requests.get('http://127.0.0.1:8000/api/v1/produtos/').json()
    return render(request, 'index.html', {'response': response})
