from django.db import models


class ProviderProfile(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=12)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)

    def __str__(self):
        """
        """
        return self.name

   
class ProviderLocation(models.Model):

    profile = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE,
                                related_name='provider_profile')
    location_name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()
    price =  models.IntegerField(max_length=20)
