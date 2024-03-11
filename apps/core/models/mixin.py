import uuid
from django.db.models import Model, UUIDField, DateTimeField


class BaseModelMixin(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
