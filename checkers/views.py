from rest_framework.viewsets import ViewSet
from checkers import serializers
from checkers import models
from rest_framework.response import Response

# Create your views here.
class BoardViewSet(ViewSet):
  serializer_class=serializers.BoardSerializer
  permission_classes=[]
  
  def list(self,request):
    boards=models.Board.objects.all()
    serializer=self.serializer_class(instance=boards,many=True)
    return Response(serializer.data)
  
  def create(self,request):
    serializer=self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
  
  def retrieve(self,request,id):
    board=models.Board.objects.get(pk=id)
    serializer=self.serializer_class(instance=board,many=False)
    return Response(serializer.data)