from django.core.urlresolvers import reverse
from django.db import models

#from usermanagement.models import User


class Enterprise(models.Model):
    #logo=models.ImageField()
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=300)
    postcode = models.CharField(max_length=50)
    city=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('enterprise_detail', args=(self.id,))

    def __str__(self):
        return self.name


class Offer(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=400, blank=True)
    profile_researched=models.TextField(max_length=400, blank=True)
    enterprise = models.ForeignKey('Enterprise')

    def get_absolute_url(self):
        return reverse('offer_detail', args=(self.id,))

    def __str__(self):
        return self.title


# class Appliance(models.Model):
#     #candidate_user = models.ForeignKey(User)
#     offer= models.ForeignKey('Offer')
#
#     #class Meta:
#         # unique_together=(  # cela va permettre une contrainte d'unicité pour empêcher d'avoir 2 même candidatures pour un même Candidat
#         #     ('candidate_user', 'offer'),
#         # )
#
#     def __str__(self):
#         return self.offer.title