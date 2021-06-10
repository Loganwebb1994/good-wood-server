from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goodwoodapi.models import GoodWoodUser
from django.contrib.auth.models import User

class ProfileView(ViewSet):



    def list(self, request):  
        goodwoodusers = GoodWoodUser.objects.all()

        
        goodwooduser = GoodWoodSerializer(
            goodwoodusers, many=True, context={'request': request}
        )

        
        return Response(goodwooduser.data)

    def retrieve(self, request, pk=None):
        try:
            goodwooduser = GoodWoodUser.objects.get(pk=pk)
            serializer = GoodWoodSerializer(goodwooduser, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


        
class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'is_staff')

class GoodWoodSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GoodWoodUser
        fields= ('id', 'phone_number', 'user')