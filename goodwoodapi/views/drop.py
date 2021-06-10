from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from goodwoodapi.models import Drop

class DropView(ViewSet):
    def create(self, request):

        drop = Drop()
        drop.wood_type = request.data["wood_type"]
        drop.cut_date = request.data["cut_date"]
        drop.arborist_id = request.data["arborist_id"]
        drop.woodworker_id = request.data["woodworker_id"]
        drop.availability = request.data["availability"]


        try:
            drop.save()
            serializer = DropSerializer(drop, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):

        try:
            drop = Drop.objects.get(pk=pk)
            serializer = DropSerializer(drop, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):  
        drops = Drop.objects.all()

        serializer = DropSerializer(
            drops, many=True, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):

        drop = Drop.objects.get(pk=pk)
        drop.wood_type = request.data["wood_type"]
        drop.cut_date = request.data["cut_date"]
        drop.arborist_id = request.data["arborist_id"]
        drop.woodworker_id = request.data["woodworker_id"]
        drop.availability = request.data["availability"]
        drop.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk=None):

        try:
            drop = Drop.objects.get(pk=pk)
            drop.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Drop.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class DropSerializer(serializers.ModelSerializer):


    class Meta:
        model = Drop
        fields = ('id', 'wood_type','cut_date','arborist_id','woodworker_id','availability')