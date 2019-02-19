from django.db import models
from django.utils import timezone


class MyBlog(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto_blog = models.TextField()
    fcreacion = models.DateTimeField(
            default=timezone.now)
    fpublicacion = models.DateTimeField(
            blank=True, null=True)

    def publicar(self):
        self.fpublicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
