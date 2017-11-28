from django.core.urlresolvers import reverse
from django.db import models


class Offer(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=400)
    profile_researched=models.TextField(max_length=400)

    def get_absolute_url(self):
        return reverse('offer_detail', args=(self.id,))
