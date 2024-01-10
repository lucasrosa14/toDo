from datetime import date

from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    createdAt = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadLine = models.DateField(verbose_name="Data de entrega", null=False, blank=False)
    finishedAt = models.DateField(null=True)

    class Meta:
        ordering = ["deadLine"]

    def markAsComplete(self):
        if not self.finishedAt:
            self.finishedAt = date.today()
            self.save()
