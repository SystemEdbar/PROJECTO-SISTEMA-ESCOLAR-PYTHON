from django.db import models
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Grade(models.Model):
    nameGrade = models.CharField(max_length=50)
    timeTable = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=False, unique=True)
    dateCreate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameGrade


def set_slug(sender, instance, *args, **kwargs):
    if instance.nameGrade and not instance.slug:
        slug = slugify(instance.nameGrade)
        while Grade.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.nameGrade, str(uuid.uuid4())[:4])
            )
        instance.slug = slug


pre_save.connect(set_slug, sender=Grade)
