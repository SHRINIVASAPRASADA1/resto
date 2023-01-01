from django.shortcuts import render, redirect
from .models import *
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import razorpay

RAZOR_KEY_ID = "rzp_test_HPR933L2nTKRBP"
RAZOR_KEY_SECRET = "9Qf2Gau5DKgdmjZ6k7GJyAlj"
rezerpay_clint = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))


# Create your views here.
def HomePage(request):
    return render(request, "app1/index.html", context={
        "food": BestMenu.objects.all(),
        "slider": CarouselSlider.objects.all(),
    })


def Auth_Signup(request):
    return render(request, "app1/login.html", context={})


def Carts(request):
    return render(request, "app1/cart.html", context={
        "cartItems": AddToCart.objects.filter(User=request.user.email).all()
    })


def TodaysMenuPage(request):
    if request.method == "POST":
        AddToCart(food_id=request.POST['ids'], User=request.user.email, title=request.POST['title'],
                  img=request.POST['img'], amount=request.POST['amount']).save()
    return render(request, "app1/TodaysMenuPage.html", context={
        "food": BestMenu.objects.all(),
    })


def DeleteCart(request, deleteid):
    AddToCart.objects.get(id=deleteid).delete()
    return redirect('cart')


def BookCartItem(request):
    print(request.POST)
    return HttpResponse(f"Your All Product addedc to order lint {request.POST['users']}")


def Pay_Ment(request):
    clint_s = rezerpay_clint.order.create({
        "amount": int(request.POST['total']) * 100, "currency": 'INR', "payment_capture": 1,
    })
    client_id = clint_s["id"]
    if request.method == "POST":
        print(request.POST)
        iter = 0
        qua=list(request.POST.getlist('quanti'))
        for item in AddToCart.objects.filter(User=request.user.email).all():
            BuyNow(product_id=item.id,
                   users=request.user.email,
                   phonenumber=request.POST['phonenumber'],
                   city=request.POST['city'],
                   state=request.POST['state'],
                   quant=qua[iter],
                   pincode=request.POST['pincode'],
                   address=request.POST['address'],
                   amount=request.POST['total']
                   ).save()
            iter += 1
        for item in AddToCart.objects.filter(User=request.user.email).all():
            AddToCart.objects.get(id=item.id).delete()
    return render(request, "app1/payment.html", context={
        "client_id": client_id,
        "api_key": RAZOR_KEY_ID,
        "payable": int(request.POST['total']),
    })


@csrf_exempt
def payment_complete(request):
    if request.method == "POST":
        if request.POST.get("razorpay_payment_id") is not None:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            result = rezerpay_clint.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                return HttpResponse("payment Done !")
            else:
                for item in AddToCart.objects.filter(User=request.user.email).all():
                    AddToCart.objects.get(id=item.id).delete()
                return HttpResponse("Failed !")
    for item in AddToCart.objects.filter(User=request.user.email).all():
        AddToCart.objects.get(id=item.id).delete()
    return HttpResponse("It's a payment page")
