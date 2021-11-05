from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View

from main_app.models import Donation, Institution, Category

User = get_user_model()


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags = 0

        # new_organisation = Institution.objects.create(name="zbrojownia", description="fajne_kule")
        # new_category = Category.objects.create(name="bron")
        # new_organisation.category.add(new_category)
        # new_organisation.save()
        # new_organisation = Institution.objects.create(name="organizacja przykładowa", description="przyklad")
        # new_category = Category.objects.create(name="kat examp")
        # new_organisation.category.add(new_category)
        # new_organisation.save()

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
        if request.user.is_authenticated:
            categories = Category.objects.all()
            organizations = Institution.objects.all()
            return render(request, "main_app/form.html", {'categories': categories, 'organizations': organizations})
        else:
            return redirect('/Login')


class Login(View):
    def get(self, request):
        return render(request, "main_app/login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(email=email):
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'main_app/login.html')
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


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')
