from django.db import models
from django.urls import reverse

from realtors.models import Realtor


class State(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class ListingManager(models.Manager):

    def get_published(self):
        return Listing.objects.filter(is_published=True)


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, blank=True, default=1)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    badrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    objects = ListingManager()

    class Meta:
        ordering = ['state']

    def get_absolute_url(self):
        return reverse('listings:listing', args=[self.id])

    def __str__(self):
        return self.title

    
class Photo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    def __str__(self):
        return self.title
