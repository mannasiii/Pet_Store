from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import View
# from urllib import request
from .models import Cart, Customer, Pet_Product, Pet
from django.db.models import Count
from .forms import CustomerRegisterForm , CustomerProfileForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'app/home.html')    #first default page 

# Create about views here.
def about(request):
    return render(request,'app/about.html')   

# Create contact views here.
def contact(request):
    return render(request,'app/contact.html')   


#CategoryView
# class CategoryView(View):
#     def get(self, request,val):
#         pet_Product = Pet_Product.objects.filter(category=val)
#         return render(request,'app/category.html',locals()) # local is built in fun to pass order local varible to catgory
    
# class Pet_name(View):
#     def get(self, request,val):
#         petname = Pet.objects.filter(category=val)
#         return render(request,'app/category.html',locals()) # local is built in fun to pass order local varible
    

#petshop ===done == done 
class Pet_pro(View):
    def get(self, request, val):
         # Query the Pet_Product model to filter objects based on the category field
        petpro = Pet_Product.objects.filter(category=val)
        product_title = Pet_Product.objects.filter(category=val).values('product_title').annotate(total=Count('product_title'))
        return render(request, 'app/category.html',locals())

#pet Pro  = done == done
class CategoryView(View):
     def get(self, request,val):
        petname = Pet.objects.filter(category=val)
        pet_title = Pet.objects.filter(category=val).values('pet_title').annotate(total=Count('pet_title'))
        return render(request,'app/petname.html',locals()) # local is built in fun to pass order local varible to catgory

#create class for product detail
class ProductDetail(View):
    def get(self, request,pk):
        petpro = Pet_Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',locals())
    
#create class for pet detail
class PetDetail(View):
    def get(self, request,pk):
        petname = Pet.objects.get(pk=pk)
        return render(request,'app/petdetail.html',locals())
    
#Create class for displaying category title
class PetCategoryTitle(View):
     def get(self, request,val):
        petname = Pet.objects.filter(pet_title=val)
        pet_title = Pet.objects.filter(category=petname[0].category).values('pet_title')
        return render(request,'app/petname.html',locals()) # local is built in fun to pass order local varible to catgory

#product category title display
class ProductCategoryTitle(View):
    def get(self, request, val):
         # Query the Pet_Product model to filter objects based on the category field
        petpro = Pet_Product.objects.filter(product_title=val)
        product_title = Pet_Product.objects.filter(category=petpro[0]).values('product_title')
        return render(request, 'app/category.html',locals())


#create  Registration
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegisterForm()
        return render(request,'app/customerregistration.html',locals())
    def post(self, request):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfully!")
        else:
            messages.warning(request,"Invalid Input data!")
        return render(request, 'app/customerregistration.html', locals())

#Profile 
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self, request):
            form = CustomerProfileForm(request.POST)
            if form.is_valid():
                user = request.user
                name = form.cleaned_data['name']
                locality = form.cleaned_data['locality']
                mobile = form.cleaned_data['mobile']
                zipcode = form.cleaned_data['zipcode']
                city = form.cleaned_data['city']
                area = form.cleaned_data['area']

                #create object  customer is our model dp col = var 
                #map all data
                reg = Customer(user=user, name=name, locality=locality, mobile=mobile, zipcode=zipcode ,city=city, area=area)
                reg.save()
                messages.success(request, "Congratulations ! Profile Save successfully..")
            else:
                messages.warning(request, "Invalid Input data")
            return render(request,'app/profile.html', locals())

#just fecth the data from db then use function 
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html' ,locals())

class updateAddress(View):  #using class cause here get and post methods & we are using customerprofileform 
    def get(self, request,pk):  #pk primary key is fectching data from db 
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add) #all data automatically filled in this section
        return render(request,'app/updateAddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode= form.cleaned_data['zipcode']
            add.city = form.cleaned_data['city']
            add.area = form.cleaned_data['area']
            add.save()
            messages.success(request,"congratulation! Profile Update Successfully")
        else:
            messages.warning(request,"Invalid Input Data ")
        return redirect('address')
        
#add to cart : Action (2 views use here)
    
    
# def add_to_cart(request):
#     user= request.user #login user
#     pet_product_id =request.GET.get('prod_id')
    
#     try:
#         Pet_Product = Pet_Product.objects.get(id=pet_product_id)
#         Cart(user=user, Pet_Product=Pet_Product).save()
#     except Pet_Product.DoesNotExist:
#         return HttpResponse("Product not found or invalid ID.")
    
#     return redirect('/cart')

def add_to_cart(request):
    print(request.GET)
    user = request.user  # Logged-in user
    Pet_Product_id= request.GET.get('petpro_id')  
    Pet_product = Pet_Product.objects.get(id=Pet_Product_id)
    Cart(user=user,Pet_Product=Pet_product).save()
    return redirect('/cart')


# def add_to_cart(request):
#     user = request.user
#     pet_product_id = request.GET.get('prod_id')

#     # Check if pet_product_id is empty
#     if not pet_product_id:
#         return HttpResponse("Product ID is missing or empty.")

#     try:
#         pet_product = Pet_Product.objects.get(id=pet_product_id)
#         Cart(user=user, Pet_Product=pet_product).save()
#     except Pet_Product.DoesNotExist:
#         return HttpResponse("Product not found or invalid ID.")
    
#     return redirect('/cart')



#     try:
#         pet_product = Pet_Product.objects.get(id=pet_product_id)  # Renamed variable to avoid conflict
#         Cart(user=user, Pet_Product=pet_product).save()
#     except Pet_Product.DoesNotExist:
#         return HttpResponse("Product not found or invalid ID.")
#     return redirect('/cart')



def show_cart(request):
    user= request.user #login user
    cart = Cart.objects.filter(user=user)
    return render(request, 'app/addtocart.html',locals())