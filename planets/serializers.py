from rest_framework import serializers  # noqa: D100

from planets.models import Planet


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Planet model."""

    class Meta:  # noqa: D106
        model = Planet
        fields = ["name", "population", "terrains", "climates"]  # noqa: RUF012
