from checkers import models
from rest_framework import serializers
from uuid import uuid4

class PieceSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  board=serializers.PrimaryKeyRelatedField(required=True,queryset=models.Board.objects.all())
  color=serializers.ChoiceField(choices=models.piece_colors,required=True)
  position_x=serializers.IntegerField(required=True)
  position_y=serializers.IntegerField(required=True)
  
  def create(self,validated_data):
    piece=models.Piece.objects.create(**validated_data)
    return piece

class BoardSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  pieces=PieceSerializer(many=True,read_only=True)
  name=serializers.CharField(required=False)
  
  def create(self,validated_data):
    board=models.Board.objects.create(**validated_data)
    return board