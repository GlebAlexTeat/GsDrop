from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField( settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING )
    Money = models.DecimalField(max_digits=6, decimal_places=2,default=0)
    Icon = models.CharField(max_length=100, help_text="Enter field documentation", null=True,default=0)
    Rang = models.DecimalField(max_digits=3, decimal_places=2,  null=True,default=0)
    Cance = models.DecimalField(max_digits=2, decimal_places=2,  null=True,default=0.98)
    User_Gun = models.TextField(help_text='Enter gun piy piy', null=True,default='')
    class Meta: 
        ordering = ["-user"]

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    @receiver(post_save, sender=User) 
    def new_user(sender, instance, created, **kwargs): 
     if created: 
        Profile.objects.create(user=instance) 
        instance.profile.save()

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



