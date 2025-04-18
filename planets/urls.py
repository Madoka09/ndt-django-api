from django.urls import path  # noqa: D100

from . import views

app_name = "planets"

urlpatterns = [
    path("load/", views.load_planet_data, name="load-planet-data"),
]
