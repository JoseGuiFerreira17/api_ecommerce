from django.db import models
from django.utils.text import slugify
from apps.core.models import BaseModelMixin


class Category(BaseModelMixin):
    name = models.CharField("nome", max_length=60)
    slug = models.SlugField("slug", unique=True)
    parent = models.ForeignKey(
        "self", blank=True, null=True, related_name="children", on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        full_path = [self.name]
        i = self.parent
        while i is not None:
            full_path.append(i.name)
            i = i.parent
        return " -> ".join(full_path[::-1])

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
