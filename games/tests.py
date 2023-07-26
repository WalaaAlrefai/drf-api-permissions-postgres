from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Game
# Create your tests here.
class GameTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    

        test_game = Game.objects.create(
            game_name="snake",
            developer=testuser1,
            description="it gets bigger as much as eat.",
        )
        test_game.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  

   
    def test_games_model(self):
        game = Game.objects.get(id=1)
        actual_owner = str(game.developer)
        actual_name = str(game.game_name)
        actual_desc = str(game.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "snake")
        self.assertEqual(
            actual_desc, "it gets bigger as much as eat."
        )

    def test_get_game_list(self):
        url = reverse("games_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        games = response.data
        self.assertEqual(len(games), 1)
        self.assertEqual(games[0]["game_name"], "snake")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("games_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_owner_can_delete_game(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("games_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
