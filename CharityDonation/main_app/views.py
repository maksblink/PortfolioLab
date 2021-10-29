from django.shortcuts import render
from django.views import View

from main_app.models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags = 0
        for donation in donations:
            bags += donation.quantity
        organizations = Institution.objects.count()
        return render(request, "main_app/index.html", {'bags': bags, 'organizations': organizations})


class AddDonation(View):
    def get(self, request):
        return render(request, "main_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "main_app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "main_app/register.html")
