from django.db import models
import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Section(models.Model):
    nameSection = models.CharField(max_length=50)
    workingDay = models.CharField(max_length=50)
    slug = models.SlugField(null=False, blank=False, unique=True)
    dateCreate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nameSection


def set_slug(sender, instance, *args, **kwargs):
    if instance.nameSection and not instance.slug:
        slug = slugify(instance.nameSection)
        while Section.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.nameSection, str(uuid.uuid4())[:4])
            )
        instance.slug = slug


pre_save.connect(set_slug, sender=Section)
