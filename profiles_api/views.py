from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication



class HelloApiView(APIView):
    """Test Api Views"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put , delete)',
        'Is similar to a traditional Django View',
        'Gives you most control over your application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!',
        'an_apiview' : an_apiview})

    def post(self,request):
        """ Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request, pk= None):
        """ Handle updating an abject"""
        return Response({'method':'PUT'})

    def patch(self,request,pk = None):
        """ Handle partial update of object """
        return Response({'method':'PATCH'})

    def delete(self,request,pk = None):
        """ Delete an object """
        return Response({'method':'DELETE'})


class HellowViewSets(viewsets.ViewSet):
    """test api viewset """
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """ return the hello message """
        a_viewset = ['uses actions (list,create,retieve,update,partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message' : 'Hello!' , 'a_viewset': a_viewset})


    def create(self,request):
        """create the new hello message """
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """ Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """handle updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request ,pk=None):
        """ handle partial update of an object """
        return Response({'http_method':'PATCH'})

    def destroy(self, request ,pk=None):
        """ handle removing an object """
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.updateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    # django framework will allow search using name or email
    search_fields = ('name' , 'email',)
