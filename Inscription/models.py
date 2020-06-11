from django.db import models
from Alumns.models import Alumn
from Grade.models import Grade
from Section.models import Section
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Inscription(models.Model):
    numberInscription = models.CharField(max_length=50)
    nameAlumn = models.OneToOneField(Alumn, max_length=50, on_delete=models.CASCADE)
    nameGrade = models.ForeignKey(Grade, max_length=50, blank=False, on_delete=models.CASCADE)
    nameSection = models.ForeignKey(Section, max_length=50, blank=False, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, blank=False, unique=True)
    dateCreate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.numberInscription


def set_slug(sender, instance, *args, **kwargs):
    if instance.numberInscription and not instance.slug:
        slug = slugify(instance.numberInscription)
        while Inscription.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.numberInscription, str(uuid.uuid4())[:4])
            )
        instance.slug = slug


pre_save.connect(set_slug, sender=Inscription)