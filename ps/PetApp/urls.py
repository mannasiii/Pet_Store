from django.urls import path
from . import views
#from .views import home, CategoryView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm , MyPasswordResetForm , MyPasswordChangeForm  , MySetPasswordForm


urlpatterns = [
    path("",views.home),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('product/<slug:val>', views.Pet_pro.as_view(), name='product'), #categoryView  is class #petproduct
    path('pets/<slug:val>/',views.CategoryView.as_view(), name='pets'),  #petName is class here #pettypes
    
    # for product and pet details
    path('productdetail/<int:pk>', views.ProductDetail.as_view(), name='productdetail'), #petproduct #petpro
    path('petdetail/<int:pk>', views.PetDetail.as_view(), name='petdetail'), #petName is class  #petname
    #CategoryTile for display category
    path('petcategory/<val>', views.PetCategoryTitle.as_view(),name='petcategory'),
    path('productcategory/<val>',views.ProductCategoryTitle.as_view(),name='productcategory'),


    #login authentication 
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name ='app/login.html' , authentication_form =LoginForm),name='login'),
    
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html' , form_class=MyPasswordChangeForm,  success_url ='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name ='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page ="login"), name ='logout'),

    #forgot password
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html' , form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/' ,auth_view.PasswordResetDoneView.as_view(template_name ='app/password_reset_done.html'),name ='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/' , auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name ='password_reset_confirm'),
    path('password-reset-complete/' ,auth_view.PasswordResetCompleteView.as_view(template_name ='app/password_reset_complete.html'), name ='password_reset_complete'),

    #manasi : profile information
    path('profile/',views.ProfileView.as_view() ,name='profile'),
    path('address/',views.address ,name='address'), #this is fun not a class
    path('updateAddtress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'), 

    #action part : Add to product 
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'), #add to product
    path('cart/', views.show_cart, name='showcart'), # after adding fetch all the product to  page

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

