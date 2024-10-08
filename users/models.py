from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    STAFF = "S"
    CUSTOMER = "C"
    USER_TYPES = (
        (STAFF, _("Staff")),
        (CUSTOMER, _("Customer")),
    )
    type = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer')
    company_name = models.CharField(_("Company Name"), max_length=100)
    address = models.CharField(_("Address"), max_length=200)
    phone = models.CharField(_("Phone Number"), max_length=50)

    def __str__(self):
        return self.company_name

    def get_absolute_url(self):
        return reverse('customer:view', kwargs={'pk': self.pk})


class Staff(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="staffs")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="staff")
    name = models.CharField(_("Full Name"), max_length=100)
    phone = models.CharField(_("Phone Number"), max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('customer:view', kwargs={'pk': self.pk})
