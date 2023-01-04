from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('auth', views.Auth_Signup, name='auth'),
    path('menufilter/querry=/<querry>', views.TodaysMenuPageFilter, name='TodaysMenuPageFilter'),
    path('cart', views.Carts, name='cart'),
    path('delete/<deleteid>', views.DeleteCart, name='delete'),
    path('cartBuy', views.BookCartItem, name='cartBuy'),
    path('payment', views.Pay_Ment, name='payment'),
    path('paymentCapturte', views.__payment_complete__single_item, name='paymentCapturte'),
    path('addtocart/<num>', views._AddToCart, name='addtocart'),
    path('deleteorder/<num>', views._deleteorder, name='deleteorder'),
    path('menu', views.TodaysMenuPage, name='menu'),
    path('payed', views.payment_complete, name='payed'),
    path('myorder', views.render_my_order, name='myorder'),
    path('logout', views.Make_Logout, name='logout'),
    path('buying....', views._render_single_item_buy, name='_render_single_item_buy'),
    path('accounts/', include('allauth.urls')),
]
