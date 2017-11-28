from django.core.urlresolvers import reverse
from django.db import models


class Enterprise(models.Model):
    #logo=models.ImageField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    postcode = models.CharField(max_length=50)
    city=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('enterprise_detail', args=(self.id,))


class Offer(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=400)
    profile_researched=models.TextField(max_length=400)
    enterprise = models.ForeignKey(Enterprise)

    def get_absolute_url(self):
        return reverse('offer_detail', args=(self.id,))

    def __str__(self):
        return self.title


