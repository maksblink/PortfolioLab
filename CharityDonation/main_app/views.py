from django.shortcuts import render
from django.views import View

from main_app.models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags = 0
        for donation in donations:
            bags += donation.quantity
        foundations = Institution.objects.filter(type='fundacja')
        organizations = Institution.objects.filter(type='organizacja pozarządowa')
        local_collection = Institution.objects.filter(type='zbiórka lokalna')
        counter = foundations.count() + organizations.count() + local_collection.count()
        return render(request, "main_app/index.html",
                      {'bags': bags, 'foundations': foundations, 'organizations': organizations,
                       'local_collection': local_collection, 'counter': counter})


class AddDonation(View):
    def get(self, request):
        return render(request, "main_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "main_app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "main_app/register.html")
