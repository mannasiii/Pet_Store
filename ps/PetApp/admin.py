from django.contrib import admin
from .models import Pet_Product , Pet , Customer ,Cart


# Register your models here.

@admin.register(Pet_Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_title', 'discounted_price', 'category', 'product_image' ] 
    
@admin.register(Pet)
class PetModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'pet_title', 'discounted_price', 'category', 'pet_image' ] 
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','locality','mobile','zipcode' ,'city' ,'area']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display =['id', 'user','Pet_Product' ,'Product_quantity', 'Pet','Pet_quantity']