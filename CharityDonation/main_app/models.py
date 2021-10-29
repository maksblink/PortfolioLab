from django.contrib.auth.models import User
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


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=128, help_text="ulica plus numer domu")
    phone_number = models.CharField(max_length=12)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=64)
    pick_up_date = models.DateTimeField(auto_now=True)
    pick_up_time = models.DateTimeField(auto_now=True)
    pick_up_comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.SET_NULL)
