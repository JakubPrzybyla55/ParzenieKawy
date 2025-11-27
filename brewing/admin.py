from django.contrib import admin
from .models import Brewer, Coffee, Recipe, RecipePhase, Profile

class RecipePhaseInline(admin.TabularInline):
    model = RecipePhase
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipePhaseInline]
    list_display = ('brewer', 'coffee', 'coffee_amount', 'grind_size')

class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('brewers', 'coffees')

admin.site.register(Brewer)
admin.site.register(Coffee)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile, ProfileAdmin)
