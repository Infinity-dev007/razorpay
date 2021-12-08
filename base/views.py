from django.shortcuts import render
import Razorpay
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = 50000

        client = Razorpay.Client(
            auth=("rzp_test_x5kWczU3FFO5E5", "XelmBbmDBQBQGGwP21r26FMM"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request, 'index.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")
