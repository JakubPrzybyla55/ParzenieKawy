from django.db import models
from django.contrib.auth.models import User

class Brewer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa zaparzacza")
    description = models.TextField(blank=True, verbose_name="Opis")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Zaparzacz"
        verbose_name_plural = "Zaparzacze"

class Coffee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa kawy")
    processing = models.CharField(max_length=100, verbose_name="Obróbka")
    country = models.CharField(max_length=100, verbose_name="Kraj")
    variety = models.CharField(max_length=100, verbose_name="Odmiana", blank=True)
    roast_level = models.CharField(max_length=100, verbose_name="Stopień palenia")

    def __str__(self):
        return f"{self.name} ({self.country})"

    class Meta:
        verbose_name = "Kawa"
        verbose_name_plural = "Kawy"

class Recipe(models.Model):
    brewer = models.ForeignKey(Brewer, on_delete=models.CASCADE, verbose_name="Zaparzacz")
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE, verbose_name="Kawa")
    coffee_amount = models.IntegerField(verbose_name="Ilość kawy (g)")
    grind_size = models.CharField(max_length=100, verbose_name="Stopień zmielenia")

    def __str__(self):
        return f"Przepis: {self.brewer} - {self.coffee}"

    class Meta:
        verbose_name = "Przepis"
        verbose_name_plural = "Przepisy"

class RecipePhase(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='phases', on_delete=models.CASCADE)
    action = models.CharField(max_length=200, verbose_name="Czynność")
    time = models.CharField(max_length=100, verbose_name="Czas (np. 30s)")
    water_amount = models.CharField(max_length=100, verbose_name="Ilość wody (g)")
    order = models.PositiveIntegerField(default=0, verbose_name="Kolejność")

    class Meta:
        ordering = ['order']
        verbose_name = "Faza parzenia"
        verbose_name_plural = "Fazy parzenia"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brewers = models.ManyToManyField(Brewer, blank=True, verbose_name="Moje zaparzacze")
    coffees = models.ManyToManyField(Coffee, blank=True, verbose_name="Moje kawy")

    def __str__(self):
        return f"Ekwipunek użytkownika {self.user.username}"
