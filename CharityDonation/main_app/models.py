from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)


institution = [
    ('fundacja', 'fundacja'),
    ('organizacja pozarządowa', 'organizacja pozarządowa'),
    ('zbiórka lokalna', 'zbiórka lokalna')]


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    type = models.CharField(choices=institution, max_length=23, default='fundacja')
    category = models.ManyToManyField(Category)
