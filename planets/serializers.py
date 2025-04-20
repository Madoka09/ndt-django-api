from rest_framework import serializers  # noqa: D100

from planets.models import Planet


class PlanetSerializer(serializers.ModelSerializer):
    """Serializer for the Planet model."""

    class Meta:  # noqa: D106
        model = Planet
        fields = ["id", "name", "population", "terrains", "climates"]  # noqa: RUF012

    def validate_name(self, value: str) -> str:  # noqa: D102
        if not value.strip():
            err = "Name value cannot be empty or be just spaces."
            raise serializers.ValidationError(err)
        return value

    def validate_population(self, value: int) -> int:  # noqa: D102
        if value is not None and value < 0:
            err = "Population value cannot be negative."
            raise serializers.ValidationError(err)
        return value

    def validate_terrains(self, value: str) -> str:  # noqa: D102
        if not value and not value.strip():
            err = "Terrains value cannot be empty or be just spaces."
            raise serializers.ValidationError(err)
        return value

    def validate_climates(self, value: str) -> str:  # noqa: D102
        if not value and not value.strip():
            err = "Climates value cannot be empty or be just spaces."
            raise serializers.ValidationError(err)
        return value
