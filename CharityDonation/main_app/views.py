from django.shortcuts import render
from django.views import View


class LandingPage(View):
    def get(self, request):
        return render(request, "main_app/index.html")


class AddDonation(View):
    def get(self, request):
        return render(request, "main_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "main_app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "main_app/register.html")
