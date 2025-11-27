from django.contrib import admin
from django.urls import path, include
from brewing import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("", views.home, name="home"),
    path("brewers/", views.browse_brewers, name="browse_brewers"),
    path("brewers/add/<int:brewer_id>/", views.add_brewer_to_inventory, name="add_brewer"),
    path("coffees/", views.browse_coffees, name="browse_coffees"),
    path("coffees/add/<int:coffee_id>/", views.add_coffee_to_inventory, name="add_coffee"),
    path("inventory/", views.inventory, name="inventory"),
    path("get-recipe/", views.get_recipe, name="get_recipe"),
]
