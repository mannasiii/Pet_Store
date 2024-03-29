from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 1st model Pet 
class Pet(models.Model):
    PET_NAME=(
    ('r','Rabits'),
    ('ck','Cats & Kitten'),
    ('dp', 'Dog & Puppies'),
    ('h', 'Hamsters, Rats'),
    ('f', 'Fish'),
    ('t','Turtle'),
    ('ho', 'Horse'),
)
    pet_title = models.CharField(max_length=150)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp =models.TextField(default='')
    #brand = models.CharField(max_length=150)
    category = models.CharField(choices=PET_NAME, max_length=2)
                             #dropdown for pet shop product category
    pet_image = models.ImageField(upload_to='pet') #img store in media direrctory in setting
    def __str__(self):
        return self.pet_title
    
#2nd Models for Pets shop
class Pet_Product(models.Model):
    CATEGORY_CHOICES = (
    ('food','Pet Food & water bowl'),
    ('Beds' ,'Dog Beds'),
    ('kit','Pet Grooming Kits'),
    ('carrier','Pet Carrier'),
    ('Stainfree' ,'Pet Stain & Order Removers'),
    ('Tr','Treats'),    
    ('med','Pet Supplements & vitamins'),
    ('pro','Pet-Friendly Cleaning Products'),
)
    product_title = models.CharField(max_length=150)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    #description = models.TextField()
    composition = models.TextField(default='')
    prodapp =models.TextField(default='')
    #brand = models.CharField(max_length=150)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
                             #dropdown for pet shop product category
    product_image = models.ImageField(upload_to='pet_product') #img store in media direrctory in setting
    def __str__(self):
        return self.product_title
    

AREA_CHOICES =(
    ('ANDHERI','Andheri'),
    ('JOGESWARI','Jogeswari'),
    ('RAM MANDIR','ram mandir'),
    ('GOREGAV', 'goregav'),
    ('MALAD','malad'),
    ('KANDIVALI','kandivali'),
    ('BORIVALI','borivali'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length =200)
    locality = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=50)
    area = models.CharField(choices = AREA_CHOICES, max_length=100)
    def __str__(self):
        return self.name

#Add To Cart 

#cart for Pet and petshop
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #first product
    Pet_Product =models.ForeignKey(Pet_Product,on_delete=models.CASCADE)
    #second product
    Pet = models.ForeignKey(Pet,on_delete=models.CASCADE)

    Product_quantity = models.PositiveIntegerField(default=1)
    
    Pet_quantity = models.PositiveIntegerField(default=1)
    @property
    def total_cost(self):
        total_cost_Product = self.Product_quantity * (self.Pet_Product.discounted_price if self.Pet_Product else 0)
        total_cost_Pet = self.Pet_quantity * (self.Pet.discounted_price if self.Pet else 0)
        return total_cost_Product + total_cost_Pet

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     Product =models.ForeignKey(Pet_Product,on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     @property
#     def total_cost(self):
#         return self.quantity * self.Product.discounted_price
        