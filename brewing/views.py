from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Brewer, Coffee, Profile, Recipe

def home(request):
    return render(request, "home.html")

@login_required
def browse_brewers(request):
    brewers = Brewer.objects.all()
    user_brewers = request.user.profile.brewers.all()
    return render(request, "brewing/browse_brewers.html", {"brewers": brewers, "user_brewers": user_brewers})

@login_required
def add_brewer_to_inventory(request, brewer_id):
    brewer = get_object_or_404(Brewer, id=brewer_id)
    request.user.profile.brewers.add(brewer)
    return redirect("browse_brewers")

@login_required
def browse_coffees(request):
    coffees = Coffee.objects.all()
    user_coffees = request.user.profile.coffees.all()
    return render(request, "brewing/browse_coffees.html", {"coffees": coffees, "user_coffees": user_coffees})

@login_required
def add_coffee_to_inventory(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)
    request.user.profile.coffees.add(coffee)
    return redirect("browse_coffees")

@login_required
def inventory(request):
    profile = request.user.profile
    return render(request, "brewing/inventory.html", {"brewers": profile.brewers.all(), "coffees": profile.coffees.all()})

@login_required
def get_recipe(request):
    recipe = None
    if request.method == "POST":
        # API Stub Logic
        # W prawdziwej aplikacji tutaj byłoby zapytanie do zewnętrznego API lub
        # bardziej skomplikowany algorytm dobierania przepisu.
        # Na razie pobieramy pierwszy lepszy przepis z bazy jako "rekomendację".
        recipe = Recipe.objects.first()

    return render(request, "brewing/get_recipe.html", {"recipe": recipe})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
