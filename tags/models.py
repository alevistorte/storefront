from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TagItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    """ 
    Define una relacion generica. De esta forma podemos reutilizar 
    nustra app y no atar las tags unicamente a produtos.
    Pata esto necesitamos dos campos: Type e ID
    Con el type, apuntamos a la tabla en cuestion y con el ID, seleccionamos
    el elemento que necesitamos de esta tabla
    Para almacenar el contenido que extraigamos debemos crear un objeto generico
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
