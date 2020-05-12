from django.db import models

class Users(models.Model):

    Name = models.CharField(max_length=20, help_text="Enter field documentation")
    Money = models.DecimalField(max_digits=6, decimal_places=2)
    Admin = models.BooleanField(default=False)
    Pass = models.CharField(max_length=20, help_text="Pass word",null=True)
    Email = models.EmailField(max_length=120, help_text="email adress", null=True)
    Icon = models.CharField(max_length=100, help_text="Enter field documentation", null=True)
    Rang = models.DecimalField(max_digits=3, decimal_places=2,  null=True)
    Cance = models.DecimalField(max_digits=2, decimal_places=2,  null=True)
    User_Gun = models.TextField(help_text='Enter gun piy piy', null=True)
    class Meta: 
        ordering = ["-Name"]

    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        return self.Name

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



