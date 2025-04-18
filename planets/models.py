from django.db import models  # noqa: D100


# Create your models here.
class Planet(models.Model):
    """Definition of the Planet instance."""

    name = models.CharField(max_length=50, blank=False, null=False)
    population = models.IntegerField(null=True)
    terrains = models.CharField(max_length=500, blank=True)
    climates = models.CharField(max_length=500, blank=True)

    def __str__(self) -> str:  # noqa: D105
        return self.name
