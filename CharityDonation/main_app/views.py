from django.contrib.auth import get_user_model, authenticate, login
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from main_app.models import Donation, Institution

User = get_user_model()


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags = 0
        for donation in donations:
            bags += donation.quantity
        foundations = Institution.objects.filter(type='fundacja')
        organizations = Institution.objects.filter(type='organizacja pozarządowa')
        local_collections = Institution.objects.filter(type='zbiórka lokalna')
        counter = foundations.count() + organizations.count() + local_collections.count()
        return render(request, "main_app/index.html",
                      {'bags': bags, 'foundations': foundations, 'organizations': organizations,
                       'local_collections': local_collections, 'counter': counter})


class AddDonation(View):
    def get(self, request):
        return render(request, "main_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "main_app/login.html")

    def post(self, request):
        # if User.objects.fileter()
            user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/Register')


class Register(View):
    def get(self, request):
        return render(request, "main_app/register.html")

    def post(self, request):
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            return render(request, "main_app/register.html", {'error': 'Passwords must be the same.'})
        try:
            new_user = User.objects.create_user(password=password,
                                                username=request.POST.get('email'),
                                                first_name=request.POST.get('name'),
                                                last_name=request.POST.get('surname'),
                                                email=request.POST.get('email'))
        except IntegrityError:
            return render(request, "main_app/register.html", {'error': 'This user already exists.'})
        except ValueError:
            return render(request, "main_app/register.html", {'error': 'You must complete all the fields.'})
        return redirect('/Login')
