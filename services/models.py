from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class ServiceType(models.Model):
    name = models.CharField(_("Name"), max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Service(models.Model):
    type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(_("Name"), max_length=100)
    description = models.CharField(_("Description"), max_length=250)
    price = models.FloatField(_("Price"))
    time = models.IntegerField(_("Minutes"))
    add_on = models.BooleanField(_("Add On"), default=False)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('services:view', kwargs={'pk': self.pk})
