from django.db import models


class FilmesA24Model(models.Model):

    titulo = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    lancamento = models.DateField()

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['id']

    def __str__(self):
        return self.titulo

class ComentariosModel(models.Model):

    filme = models.ForeignKey(FilmesA24Model, related_name='comentarios', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    comentario = models.TextField(max_length=255, blank=True, default='')
    data = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['id']