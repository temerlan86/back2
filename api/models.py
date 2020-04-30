from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=Category, blank=True, null=True)
    title = models.CharField(max_length=99999)
    image = models.CharField(max_length=99999)
    text = models.CharField(max_length=99999)