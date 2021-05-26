from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


# Create your models here.
class Identifier(models.Model):
    id = models.UUIDField(_('ID'), default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(_('Date Created'), auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '{} - {}'.format(self.id, self.created_at)
