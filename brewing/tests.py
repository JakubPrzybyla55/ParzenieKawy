from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Brewer, Coffee, Recipe, Profile

class CoffeeAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.brewer = Brewer.objects.create(name="V60", description="Drip")
        self.coffee = Coffee.objects.create(name="Ethiopia", processing="Washed", country="Ethiopia", roast_level="Light")
        self.recipe = Recipe.objects.create(
            brewer=self.brewer,
            coffee=self.coffee,
            coffee_amount=20,
            grind_size="Medium"
        )

    def test_profile_created_signal(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_inventory_add_brewer(self):
        response = self.client.get(f'/brewers/add/{self.brewer.id}/')
        self.assertRedirects(response, '/brewers/')
        self.assertTrue(self.user.profile.brewers.filter(id=self.brewer.id).exists())

    def test_inventory_add_coffee(self):
        response = self.client.get(f'/coffees/add/{self.coffee.id}/')
        self.assertRedirects(response, '/coffees/')
        self.assertTrue(self.user.profile.coffees.filter(id=self.coffee.id).exists())

    def test_get_recipe_view(self):
        response = self.client.post('/get-recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rekomendowany Przepis")
        self.assertContains(response, "V60")
