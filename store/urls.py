from django.urls import path
from . import views
from store.views import add_to_cart


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('signin/', views.user_login, name='signin'),
    path('logout/', views.user_logout, name='logout'),
    path('products/', views.product_list, name='products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='cart_add'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
