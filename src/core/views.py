from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

# third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostView(
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
       return self.list(self, request, *args, **kwargs)
    
    # def perform_create(self, serializer):
    #     # send an email
    #     serializer.save()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
 # class TestView(APIView):
 #    permission_classes = (IsAuthenticated,)
 #    def get(self, request, *args, **kwargs):
 #        
 #            #'name': 'john',
 #             #'age': 23
 #        qs = Post.objects.all()
 #        post = qs.first()
 #        #serializer = PostSerializer(qs, many=True)
 #        serializer = PostSerializer(post)
 #        return Response(serializer.data)
 #    
 #    def post(self, request, *args, **kwargs):
 #        serializer = PostSerializer(data=request.data)
 #        if serializer.is_valid():
 #            serializer.save()
 #            return Response(serializer.data)
 #        return Response(serializer.errors)

#def test_view(request):
#    data = {
#        'name': 'john',
#        'age': 23
#    }
#    return JsonResponse(data)