from django.conf import settings
from django.db import models


class UserMixin(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    image_url = models.URLField()

    class Meta:
        abstract = True


class NameDescriptionMixin(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(
        max_length=256,
        null=False, default='', blank=True,
    )

    class Meta:
        abstract = True


class Category(UserMixin, NameDescriptionMixin, ImageMixin, models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'


class Plant(UserMixin, NameDescriptionMixin, models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    watering_interval = models.PositiveIntegerField(
        help_text='In seconds'
    )
    fertilizing_interval = models.PositiveIntegerField(
        help_text='In seconds'
    )

    EXPOSURE_CHOICES = [
        ('dark', 'Dark'),
        ('shade', 'Shade'),
        ('partsun', 'Part sun'),
        ('fullsun', 'Full sun'),
    ]

    required_exposure = models.CharField(
        max_length=16,
        choices=EXPOSURE_CHOICES,
        help_text="Amount of sun"
    )

    HUMIDITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    required_humidity = models.CharField(
        max_length=10,
        choices=None,
        help_text="Optimal humidity"
    )

    TEMPERATURES_CHOICES = [
        ('cold', 'Cold'),
        ('medium', 'Medium'),
        ('warm', 'Warm'),
    ]
    required_temperature = models.CharField(
        max_length=16,
        choices=None,
        help_text="Optimal temperature"
    )
    blooming = models.BooleanField(
        default=False,
        null=False, blank=True,
    )

    DIFFICULTY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium-low'),
        (3, 'Medium'),
        (4, 'Medium-high'),
        (5, 'High'),
    ]
    difficulty = models.CharField(
        max_length=16,
        choices=DIFFICULTY_CHOICES,
        default=1,
        verbose_name='Cultivation difficulty'
    )


class Room(UserMixin, NameDescriptionMixin, models.Model):

    EXPOSURE_CHOICES = Plant.EXPOSURE_CHOICES
    exposure = models.CharField(
        max_length=10,
        choices=EXPOSURE_CHOICES,
        help_text="Amount of sun"
    )
    HUMIDITY_CHOICES = Plant.HUMIDITY_CHOICES
    humidity = models.CharField(
        max_length=10,
        choices=HUMIDITY_CHOICES,
        help_text="Optimal humidity"
    )

    TEMPERATURES_CHOICES = Plant.TEMPERATURES_CHOICES
    temperature = models.CharField(
        max_length=10,
        choices=TEMPERATURES_CHOICES,
        help_text="Optimal temperature"
    )
    drafty = models.BooleanField(
        default=False, null=False, blank=True,
    )


class UserPlant(UserMixin, NameDescriptionMixin, ImageMixin, models.Model):

    room = models.ForeignKey(
        Room, on_delete=models.PROTECT,
    )
    plant = models.ForeignKey(
        Plant, on_delete=models.PROTECT,
        verbose_name='Type of plant',
    )
    last_fertilized = models.DateTimeField(
        null=True, blank=True,
    )
    last_watered = models.DateTimeField(
        null=True, blank=True,
    )
