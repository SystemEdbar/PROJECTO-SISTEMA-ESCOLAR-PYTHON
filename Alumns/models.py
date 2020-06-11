from django.db import models
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Alumn(models.Model):
    carnetAlumn = models.CharField(max_length=18)
    nameAlumn = models.CharField(max_length=50)
    surnameAlumn = models.CharField(max_length=50)
    directionAlumn = models.TextField(max_length=75)
    slug = models.SlugField(null=False, blank=False, unique=True)
    imageAlumn = models.ImageField(upload_to='alumns/', null=False, blank=False)
    dateCreate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameAlumn


def set_slug(sender, instance, *args, **kwargs):
    if instance.carnetAlumn and not instance.slug:
        slug = slugify(instance.carnetAlumn)
        while Alumn.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.carnetAlumn, str(uuid.uuid4())[:4])
            )
        instance.slug = slug


pre_save.connect(set_slug, sender=Alumn)
