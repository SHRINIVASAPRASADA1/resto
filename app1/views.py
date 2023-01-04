from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout
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
        print(request.POST)
    return render(request, "app1/TodaysMenuPage.html", context={
        "food": BestMenu.objects.order_by('-Ratting').all(),
        "catogory":catogory.objects.order_by('-title').all()
    })


def _AddToCart(request, num):
    data = BestMenu.objects.get(id=num)
    AddToCart(food_id=data.id, User=request.user.email, title=data.Title,
              img=data.img.url, amount=data.amount).save()
    return redirect('menu')


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
        qua = list(request.POST.getlist('quanti'))
        for item in AddToCart.objects.filter(User=request.user.email).all():
            myimg = BestMenu.objects.get(id=item.food_id)
            BuyNow(product_id=item.id,
                   users=request.user.email,
                   phonenumber=request.POST['phonenumber'],
                   city=request.POST['city'],
                   state=request.POST['state'],
                   quant=qua[iter],
                   pincode=request.POST['pincode'],
                   address=request.POST['address'],
                   amount=request.POST['total'],
                   img=myimg.img.url,
                   title=myimg.Title,
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
                return redirect('myorder')
            else:
                for item in AddToCart.objects.filter(User=request.user.email).all():
                    AddToCart.objects.get(id=item.id).delete()
                return Http404("<h1 > Failed ! </h1> !")
    return redirect('myorder')


def render_my_order(request):
    return render(request, "app1/MyOrders.html", context={
        "order": BuyNow.objects.filter(users=request.user.email).all()
    })


def _deleteorder(request, num):
    BuyNow.objects.get(id=num).delete()
    return redirect('myorder')


def _render_single_item_buy(request):
    if request.method == "POST":
        item = BestMenu.objects.get(id=request.POST['selected'])
        BuyNow(product_id=item.id,
               users=request.user.email,
               phonenumber=request.POST['numbers'],
               city=request.POST['city'],
               state=request.POST['state'],
               quant=1,
               pincode=request.POST['pincode'],
               address=request.POST['address'],
               amount=item.amount,
               img=item.img.url,
               title=item.Title,
               ).save()
        clint_s = rezerpay_clint.order.create({
            "amount": int(item.amount) * 100, "currency": 'INR', "payment_capture": 1,
        })
        client_id = clint_s["id"]
        return render(request, "app1/paymentcapture.html", context={
            "client_id": client_id,
            "api_key": RAZOR_KEY_ID,
            "payable": int(item.amount),
        })
    return redirect("index")


@csrf_exempt
def __payment_complete__single_item(request):
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
                return redirect('myorder')
            else:
                BuyNow.objects.all().last().delete()
                return HttpResponse("Failed !")
    BuyNow.objects.all().last().delete()
    return HttpResponse("It's a payment page")


def TodaysMenuPageFilter(request,querry):
    print(querry)
    return render(request, "app1/TodaysMenuPage.html", context={
        "food": BestMenu.objects.all().filter(catogorys__title=querry),
        "catogory":catogory.objects.order_by('-title').all()
    })

# catogorys__name__contains = str(querry)

def Make_Logout(request):
    logout(request)
    return redirect('index')



def addRattings():
    
    pass