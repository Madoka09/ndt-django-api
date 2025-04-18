import urllib.parse  # noqa: D100

import requests
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from planets.models import Planet
from planets.serializers import PlanetSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    """Viewset used to perform CRUD operations on a Planet object."""

    queryset = Planet.objects.all().order_by("id")
    serializer_class = PlanetSerializer

@api_view(["GET"])
def load_planet_data() -> Response:
    """Get and save the initial batch of data to populate the table.

    Gets the planet data form the GraphQL API endpoint using a get request
    and populates the database, if a single instance of Planet exists
    the request is rejected.

    Returns:
        Response: returns 201 status if the data was created succesfully.
            or a 403 status if there was data loaded.

    """
    query_data = """
        query {
            allPlanets {
                planets {
                    name
                    population
                    terrains
                    climates
                }
            }
        }
    """

    url_params = {"query": query_data}
    encoded_url = urllib.parse.urlencode(url_params)

    url = f"https://swapi-graphql.netlify.app/.netlify/functions/index?{encoded_url}"

    response = requests.get(url, headers={"Accept": "application/json"}, timeout=300)

    json_encoded_res = response.json()["data"]["allPlanets"]["planets"]

    #Dinamically load the data to the databse if there are no objects loaded
    all_planets = Planet.objects.all()

    if not len(all_planets):
        for planet in json_encoded_res:
            Planet.objects.create(
                name=planet["name"],
                population=planet["population"],
                terrains=planet["terrains"],
                climates=planet["climates"],
            )

        response_data = {
            "message": "The initial data has been created successfully",
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

    response_data = {
        "message": "The initial data was already loaded",
    }

    return Response(response_data, status=status.HTTP_403_FORBIDDEN)
