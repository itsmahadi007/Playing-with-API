from django.shortcuts import render
from django.http import JsonResponse
from .models import testdb
from .serializers import testDBSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

# Create your views here.


def apioverview(request):
    return JsonResponse("API TEST", safe=False)


class test(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request):
        obj = testdb.objects.all()
        serializer = testDBSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer_obj = testDBSerializer(data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)


class testdetails(APIView):
    def get(self, request, id):
        try:
            obj = testdb.objects.get(id=id)
        except testdb.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        seri_obj = testDBSerializer(obj)
        return Response(seri_obj.data)

    def put(self, request, id):

        try:
            obj = testdb.objects.get(id=id)
        except testdb.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        seri_obj = testDBSerializer(obj, data=request.data)
        if seri_obj.is_valid():
            seri_obj.save()
            return Response(seri_obj.data)
        return Response(seri_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = testdb.objects.get(id=id)
        except testdb.DoesNotExist:
            raise Http404
        obj = testdb.objects.get(id=id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
