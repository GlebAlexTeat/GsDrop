from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):

    user = models.OneToOneField( settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING )
    Money = models.DecimalField(max_digits=6, decimal_places=2)
    Icon = models.CharField(max_length=100, help_text="Enter field documentation", null=True)
    Rang = models.DecimalField(max_digits=3, decimal_places=2,  null=True)
    Cance = models.DecimalField(max_digits=2, decimal_places=2,  null=True)
    User_Gun = models.TextField(help_text='Enter gun piy piy', null=True)
    class Meta: 
        ordering = ["-user"]

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Gun(models.Model):
    title_gun = models.CharField(max_length=40, help_text="Enter field documentation")
    grade = models.CharField(max_length=40, help_text="качество оружия common uncommon...")
    quality  = models.CharField(max_length=40, help_text="качество оружия с завода, после полевых....")
    img_road_gun = models.CharField(max_length=100, help_text="Enter field documentation")
    value = models.DecimalField(max_digits=6, decimal_places=2)
    startrec = models.BooleanField(default=False)

class Case(models.Model):
    title = models.CharField(max_length=40, help_text="Enter field documentation")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    img_road = models.CharField(max_length=100, help_text="Enter field documentation")
    guns = models.ManyToManyField(Gun)



