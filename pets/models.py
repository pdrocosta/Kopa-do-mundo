from django.db import models


class SexOptions(models.TextChoices):
    MALE = "Male"
    DEFAULT = "Not Informed"
    FEMALE = "Female"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=20, choices=SexOptions.choices,
                           default=SexOptions.DEFAULT)
    group = models.ForeignKey("groups.Group", on_delete=models.PROTECT,
                              related_name="pets")
    traits = models.ManyToManyField("traits.Trait", related_name="pets")
