from django.conf import settings
from django.db import models


class UserMixin(models.Model):
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.PROTECT,
	)

	class Meta:
		abstract = True


class Category(UserMixin, models.Model):
	name = models.CharField(max_length=128)
	description = models.CharField(
		max_length=256,
		null=False, default='', blank=True,
	)
	slug = models.SlugField()
	image_url = models.URLField()


class Plant(UserMixin, models.Model):
	name = models.CharField(max_length=128)
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
		('partsun', 'Part sunny'),
		('fullsun', 'Full sunny'),
	]

	required_exposure = models.CharField(
		max_length=10,
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
		max_length=10,
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
		choices=DIFFICULTY_CHOICES,
		default=1,
		verbose_name='Cultivation difficulty'
	)


class Room(UserMixin, models.Model):
	name = models.CharField(max_length=128)

	EXPOSURE_CHOICES = [
		('dark', 'Dark'),
		('shade', 'Shade'),
		('partsun', 'Part sunny'),
		('fullsun', 'Full sunny'),
	]
	exposure = models.CharField(
		max_length=10,
		choices=EXPOSURE_CHOICES,
		help_text="Amount of sun"
	)
	HUMIDITY_CHOICES = [
		('low', 'Low'),
		('medium', 'Medium'),
		('high', 'High'),
	]
	humidity = models.CharField(
		max_length=10,
		choices=None,
		help_text="Optimal humidity"
	)

	TEMPERATURES_CHOICES = [
		('cold', 'Cold'),
		('medium', 'Medium'),
		('warm', 'Warm'),
	]
	temperature = models.CharField(
		max_length=10,
		choices=None,
		help_text="Optimal temperature"
	)
	drafty = models.BooleanField(
		default=False, null=False, blank=True,
	)


class UserPlant(UserMixin, models.Model):
	name = models.CharField(max_length=128)
	description = models.CharField(
		max_length=256,
		null=False, default='', blank=True,
	)
	room = models.ForeignKey(
		Room, on_delete=models.PROTECT,
	)
	plant = models.ForeignKey(
		Plant, on_delete=models.PROTECT,
	)
	fertilizing_time = models.DateTimeField()
	watering_time = models.DateTimeField()


