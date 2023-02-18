from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from .models import Game, Developer, Genre


class IndexViewTest(TestCase):
    def test_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "games/index.html")


class GameViewTest(TestCase):
    fixtures = ["game.json", "developer.json", "genre.json"]

    def setUp(self):
        self.games = Game.objects.all()

    def test_list(self):
        response = self.client.get(reverse("games:games"))
        self._common_test(response)
        self.assertEqual(
            list(response.context_data["object_list"]), list(self.games[:1])
        )

    def test_list_with_developer(self):
        developer = Developer.objects.first()
        path = reverse("games:developer", kwargs={"developer_id": developer.id})
        response = self.client.get(path)

        self._common_test(response)
        self.assertEqual(
            list(response.context_data["object_list"]),
            list(self.games.filter(developer=developer.id)),
        )

    def test_list_with_genre(self):
        genre = Genre.objects.first()
        path = reverse("games:genre", kwargs={"genre_id": genre.id})
        response = self.client.get(path)

        self._common_test(response)
        self.assertEqual(
            list(response.context_data["object_list"]),
            [game for game in self.games if game.genre.filter(id=genre.id)][:1],
        )

    def _common_test(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "games/games.html")
