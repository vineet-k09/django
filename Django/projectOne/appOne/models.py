from django.db import models
from django.urls import reverse

class Student(models.Model):
    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class TaskBoard(models.Model):
    taskName = models.CharField(max_length=100)
    taskDescription = models.TextField(max_length=100)