from rest_framework.routers import DefaultRouter
from checkers import views

checkersRouter = DefaultRouter()
checkersRouter.register(r"checkers/board",viewset=views.BoardViewSet,basename='checkers-board')