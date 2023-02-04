from django.urls import path

from .views import games


urlpatterns = [
    path("", games, name="games"),
    path("genre/<int:genre_id>", games, name="genre"),
    path("developers/<int:developer_id>", games, name="developer"),
    path("page/<int:page>/", games, name="page"),
]
