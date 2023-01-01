from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('auth', views.Auth_Signup, name='auth'),
    path('cart', views.Carts, name='cart'),
    path('delete/<deleteid>', views.DeleteCart, name='delete'),
    path('cartBuy', views.BookCartItem, name='cartBuy'),
    path('payment', views.Pay_Ment, name='payment'),
    path('menu', views.TodaysMenuPage, name='menu'),
    path('payed', views.payment_complete, name='payed'),
    path('accounts/', include('allauth.urls')),
]
