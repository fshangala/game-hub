from django.db import models
from uuid import uuid4

# Create your models here.
class Board(models.Model):
  name=models.CharField(max_length=250,default=uuid4)

piece_colors=(
  ("WHITE","White"),
  ("BLACK","Black"),
)
class Piece(models.Model):
  board=models.ForeignKey(to=Board,on_delete=models.CASCADE,related_name='pieces')
  color=models.CharField(max_length=200,choices=piece_colors)
  position_x=models.IntegerField()
  position_y=models.IntegerField()