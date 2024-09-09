from django.db import models


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    is_deleted = models.BooleanField(default=False)

    
    objects = models.Manager()

    class Meta:
        abstract = True

    def __str__(self):
        try:
            return str(self.name)
        except Exception:
            return str(self.id)

  

