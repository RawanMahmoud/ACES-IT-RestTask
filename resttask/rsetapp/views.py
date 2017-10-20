from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import committee
from .models import member
from rest_framework import mixins
from rest_framework import generics

from .serializers import committeeSerializer
from .serializers import memberSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
# Create your views here.


class committeeList(generics.ListCreateAPIView):

    queryset = committee.objects.all()
    serializer_class = committeeSerializer




class committeeDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = committee.objects.all()
    serializer_class = committeeSerializer




class memberList(generics.ListCreateAPIView):

     queryset= member.objects.all()
     serializer_class = memberSerializer



class memberDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = member.objects.all()
    serializer_class = memberSerializer



#class committeeList(APIView):

    #def get(self, request, format=None):

          # committes = committee.objects.all()
          # serializer = committeeSerializer(committes, many=True)

          # return Response(serializer.data)


   # def post(self, request, format=None):
       # serializer = committeeSerializer(data=request.data)
        #if serializer.is_valid():
          #  serializer.save()
          #  return Response(serializer.data, status=status.HTTP_201_CREATED)
       # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class memberList(APIView):
#
#     def get(self, request, format=None):
#             members = member.objects.all()
#             serializer = memberSerializer(members, many=True)
#
#             return Response(serializer.data)
#
#     def post(self, request, format=None):
#             serializer = memberSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class committeeDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, name):
#         try:
#             return committee.objects.get(pk=name)
#         except committee.DoesNotExist:
#             raise Http404
#
#     def get(self, request, name, format=None):
#         snippet = self.get_object(name)
#         serializer = committeeSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, name, format=None):
#         snippet = self.get_object(name)
#         serializer = committeeSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, name, format=None):
#         snippet = self.get_object(name)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class committeeDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = committee.objects.all()
#     serializer_class = committeeSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)