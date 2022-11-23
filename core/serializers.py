from rest_framework import serializers
from .models import FilmesA24Model, ComentariosModel

class ComentariosSerializers(serializers.ModelSerializer):

    class Meta:
        model = ComentariosModel
        fields = [
            'id',
            'filme',
            'nome',
            'comentario',
            'data'
        ]

    def validate_nome(self, valor):
        if valor == valor.title():
            return valor
        raise serializers.ValidationError('O nome precisa iniciar com letra maiúscula.')


class FilmesSerializer(serializers.ModelSerializer):

    comentarios = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comentariosmodel-detail'
    )

    class Meta:
        model = FilmesA24Model
        fields = (
            'id',
            'titulo',
            'diretor',
            'lancamento',
            'comentarios'
        )
