from django.db import models

from .utils import generate_slug


class ModelBase(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return '{model_name}, id={id}, slug={slug}'.format(
            model_name=self.__class__.__name__, id=self.id, slug=self.slug
        )


class ModelSlugBase(ModelBase):
    slug = models.SlugField(max_length=128, allow_unicode=True, unique=True, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False,
             using=None, update_fields=None):

        if self.slug in (None, ''):
            self.slug = generate_slug(type(self), length=8)
            if update_fields is not None:
                update_fields = list(update_fields)
                update_fields.append('slug')

        return super().save(force_insert=force_insert, force_update=force_update,
                            using=using, update_fields=update_fields)


class ModelTimeStampBase(ModelSlugBase):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_time',)
