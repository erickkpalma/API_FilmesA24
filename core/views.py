""" imports para API versão 1 """
from rest_framework import generics
from rest_framework.generics import get_object_or_404

""" imports para API versão 2 """
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .permissions import SuperUser
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

""" imports para ambas views """
from .models import FilmesA24Model, ComentariosModel
from .serializers import FilmesSerializer, ComentariosSerializers

""" API versão 1 """

class FilmesAPIView(generics.ListCreateAPIView):

    queryset = FilmesA24Model.objects.all()
    serializer_class = FilmesSerializer

class FilmeAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = FilmesA24Model.objects.all()
    serializer_class = FilmesSerializer


class ComentariosAPIView(generics.ListCreateAPIView):

    queryset = ComentariosModel.objects.all()
    serializer_class = ComentariosSerializers

    def get_queryset(self):
        if self.kwargs.get('filme_pk'):
            return self.queryset.filter(filme_id=self.kwargs.get('filme_pk'))
        return self.queryset.all()


class ComentarioAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = ComentariosModel.objects.all()
    serializer_class = ComentariosSerializers

    def get_object(self):
        if self.kwargs.get('comentario_pk'):
            return get_object_or_404(self.get_queryset(), filme_id=self.kwargs.get('filme_pk'),
                                     pk=self.kwargs.get('comentario_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('comentario_pk'))

""" API versão 2 """

class FilmesView(viewsets.ModelViewSet):
    queryset = FilmesA24Model.objects.all()
    serializer_class = FilmesSerializer
    permission_classes = (SuperUser, DjangoModelPermissionsOrAnonReadOnly)

    @action(methods=['get'], detail=True)
    def comentarios(self, request, pk=None):
        self.pagination_class.page_size = 1
        comentarios = ComentariosModel.objects.filter(filme_id=pk)
        page = self.paginate_queryset(comentarios)

        if page is not None:
            serializer = ComentariosSerializers(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ComentariosSerializers(comentarios, many=True)
        return Response(serializer.data)

class ComentariosView(
           mixins.CreateModelMixin,
           mixins.RetrieveModelMixin,
           mixins.UpdateModelMixin,
           mixins.DestroyModelMixin,
           mixins.ListModelMixin,
           viewsets.GenericViewSet
            ):

            queryset = ComentariosModel.objects.all()
            serializer_class = ComentariosSerializers
            permission_classes = (SuperUser, DjangoModelPermissionsOrAnonReadOnly)

