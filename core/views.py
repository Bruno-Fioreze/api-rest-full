from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Artigo
from .serializers import ArtigoSerializer


@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["GET","POST"])
def lista_de_artigos(request):


    if(request.method == "GET"):

        artigos = Artigo.objects.all()
        serializer = ArtigoSerializer(artigos,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif (request.method == "POST"):

        serializer = ArtigoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["GET","PUT","DELETE"])
def artigo_detalhe(request,pk):
    try:
        artigo = Artigo.objects.get(pk=pk)
    except Artigo.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method == "GET"):
        serializer = ArtigoSerializer(artigo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif(request.method == "PUT"):
        data = JSONParser().parse(request)
        serializer = ArtigoSerializer(artigo,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif (request.method == "DELETE"):
        artigo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
