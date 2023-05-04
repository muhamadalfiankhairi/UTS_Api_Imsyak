from django.shortcuts import render
from . models import JadwalModels
from . serializers import jadwalSerializer
# rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics 


# menampilkan semua data
@api_view(['GET']) 
def readJadwal(request):
    jadwalimsyak = JadwalModels.objects.all() 
    serializer = jadwalSerializer(jadwalimsyak, many=True) 
    return Response(serializer.data)

# menampilkan 1 data atau detail
@api_view(['GET'])
def detailJadwal(request,id):
    jadwalimsyak = JadwalModels.objects.get(pk=id) 
    serializer = jadwalSerializer(jadwalimsyak, many=False)
    return Response(serializer.data)

# menambah/input data
@api_view(['POST'])
def createJadwal(request):
    serializer = jadwalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# mengedit/update data
@api_view(['PUT'])
def updateJadwal(request,id):
    jadwalimsyak = JadwalModels.objects.get(pk=id)
    serializer=jadwalSerializer(instance=jadwalimsyak, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# meghapus/delet
@api_view(['DELETE'])
def deletJadwal(request,id):
    jadwalimsyak = JadwalModels.objects.get(pk=id)
    jadwalimsyak.delete()

    return Response('Data sudah dihilangkan')
