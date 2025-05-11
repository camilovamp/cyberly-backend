from django.db import models
import datetime
import uuid

# Create your models here.
class BaseModel(models.Model):
    class Meta:
        abstract = True

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.date_updated = datetime.datetime.now()
        return super().save(*args, **kwargs)